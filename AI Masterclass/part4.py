from manim import *
import numpy as np

class Part4ActivationNew(Scene):
    def construct(self):
        self.camera.background_color = "#0A0A0A"

        title = Text("PART 4: ACTIVATION FUNCTIONS", font_size=40, weight=BOLD).to_corner(UL)
        self.play(Write(title))

        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={"stroke_color": GREY_D, "stroke_width": 1, "stroke_opacity": 0.2},
            axis_config={"stroke_color": GREY_D, "stroke_width": 1, "stroke_opacity": 0.2}
        )
        self.play(FadeIn(grid), run_time=1.5)

        axes_lin = Axes(
            x_range=[-4, 4, 1], y_range=[-2, 6, 1],
            x_length=7, y_length=6,
            axis_config={"include_tip": False, "color": WHITE}
        ).move_to(ORIGIN).shift(DOWN * 0.2)

        x_lbls_lin = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_lin.c2p(i, 0), DOWN, buff=0.2) for i in [-2, 2, 4]])
        y_lbls_lin = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_lin.c2p(0, i), LEFT, buff=0.2) for i in [-1, 2, 4, 6]])

        lin_func = lambda x: 1.5 * x
        lin_curve = axes_lin.plot(lin_func, color=GREY_B, stroke_width=4)

        self.play(Create(axes_lin), FadeIn(x_lbls_lin), FadeIn(y_lbls_lin))
        self.play(Create(lin_curve), run_time=1.5)
        self.wait(1)

        self.play(
            axes_lin.animate.shift(LEFT * 3),
            x_lbls_lin.animate.shift(LEFT * 3),
            y_lbls_lin.animate.shift(LEFT * 3),
            lin_curve.animate.shift(LEFT * 3),
            run_time=1.5
        )

        title_lin = Text("Linear Function", font_size=32, color=GREY_B, weight=BOLD).shift(RIGHT * 3.5 + UP * 1.5)
        eq_lin = MathTex("z = Wx + b", font_size=60).next_to(title_lin, DOWN, buff=0.5)
        self.play(Write(title_lin), Write(eq_lin))

        active_axes = [axes_lin]
        active_func = [lin_func]
        x_val = ValueTracker(0)

        dot_x = Dot(color=BLUE, radius=0.08)
        dot_c = Dot(color=YELLOW, radius=0.08)
        dot_y = Dot(color=GREEN, radius=0.08)
        line_v = Line(stroke_color=GREY_C, stroke_width=2, stroke_opacity=0.5)
        line_h = Line(stroke_color=GREY_C, stroke_width=2, stroke_opacity=0.5)

        proj_group = VGroup(line_v, line_h, dot_x, dot_c, dot_y)

        def update_proj(mob):
            ax = active_axes[0]
            func = active_func[0]
            x = x_val.get_value()
            y = func(x)

            p_x = ax.c2p(x, 0)
            p_c = ax.c2p(x, y)
            p_y = ax.c2p(0, y)

            dot_x.move_to(p_x)
            dot_c.move_to(p_c)
            dot_y.move_to(p_y)

            if np.linalg.norm(p_c - p_x) > 1e-4:
                line_v.set_opacity(0.5)
                line_v.put_start_and_end_on(p_x, p_c)
            else:
                line_v.set_opacity(0)

            if np.linalg.norm(p_y - p_c) > 1e-4:
                line_h.set_opacity(0.5)
                line_h.put_start_and_end_on(p_c, p_y)
            else:
                line_h.set_opacity(0)

        proj_group.add_updater(update_proj)
        self.add(proj_group)

        self.play(x_val.animate.set_value(2), run_time=1.5)
        self.play(x_val.animate.set_value(-1.3), run_time=2)
        self.play(x_val.animate.set_value(3.5), run_time=2)

        text_lin = Text(
            "Without constraints, the output\nscales infinitely. It cannot\nlearn complex boundaries.",
            font_size=26, color=WHITE, line_spacing=1.2
        ).next_to(eq_lin, DOWN, buff=0.8)

        self.play(Write(text_lin))
        self.wait(2)
        self.play(FadeOut(text_lin), FadeOut(title_lin), FadeOut(eq_lin))

        axes_sig = Axes(
            x_range=[-5, 5, 1], y_range=[-0.2, 1.2, 0.5],
            x_length=7, y_length=6,
            axis_config={"include_tip": False, "color": WHITE}
        ).move_to(axes_lin)

        x_lbls_sig = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_sig.c2p(i, 0), DOWN, buff=0.2) for i in [-4, -2, 2, 4]])
        y_lbls_sig = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_sig.c2p(0, i), LEFT, buff=0.2) for i in [0, 0.5, 1]])

        sig_func = lambda x: 1 / (1 + np.exp(-x))
        sig_curve = axes_sig.plot(sig_func, color=PURPLE_A, stroke_width=5)

        title_sig = Text("Sigmoid Function", font_size=32, color=PURPLE_A, weight=BOLD).shift(RIGHT * 3.5 + UP * 1.5)
        eq_sig = MathTex(r"a = \frac{1}{1 + e^{-z}}", font_size=55, color=PURPLE_A).next_to(title_sig, DOWN, buff=0.5)

        x_val.set_value(0)
        active_axes[0] = axes_sig
        active_func[0] = sig_func

        self.play(
            ReplacementTransform(axes_lin, axes_sig),
            ReplacementTransform(x_lbls_lin, x_lbls_sig),
            ReplacementTransform(y_lbls_lin, y_lbls_sig),
            ReplacementTransform(lin_curve, sig_curve),
            Write(title_sig), Write(eq_sig),
            run_time=1.5
        )

        text_sig_1 = Text(
            "Input (X) is heavily mapped.\nOutput (Y) is forced between 0 and 1.",
            font_size=24, color=WHITE, line_spacing=1.2
        ).next_to(eq_sig, DOWN, buff=0.8)

        self.play(Write(text_sig_1))

        self.play(x_val.animate.set_value(4.5), run_time=2.5)
        self.play(x_val.animate.set_value(-4.5), run_time=3)
        self.wait(1)

        text_sig_2 = Text(
            "Flaw: At extreme X values,\nY barely moves.\nGradient = 0. AI stops learning.",
            font_size=24, color=RED, line_spacing=1.2, weight=BOLD
        ).move_to(text_sig_1)

        flat_left = axes_sig.plot(sig_func, x_range=[-5, -3], color=RED, stroke_width=8)
        flat_right = axes_sig.plot(sig_func, x_range=[3, 5], color=RED, stroke_width=8)

        self.play(
            ReplacementTransform(text_sig_1, text_sig_2),
            Create(flat_left), Create(flat_right)
        )
        self.play(x_val.animate.set_value(-5), run_time=1)
        self.play(x_val.animate.set_value(5), run_time=3)
        self.wait(2)

        self.play(FadeOut(text_sig_2), FadeOut(title_sig), FadeOut(eq_sig))

        axes_relu = Axes(
            x_range=[-5, 5, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=6,
            axis_config={"include_tip": False, "color": WHITE}
        ).move_to(axes_sig)

        x_lbls_relu = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_relu.c2p(i, 0), DOWN, buff=0.2) for i in [-4, -2, 2, 4]])
        y_lbls_relu = VGroup(*[MathTex(str(i), font_size=24).next_to(axes_relu.c2p(0, i), LEFT, buff=0.2) for i in [-1, 1, 3, 5]])

        relu_func = lambda x: np.maximum(0, x)
        relu_curve = axes_relu.plot(relu_func, color=GREEN, stroke_width=5)

        title_relu = Text("ReLU Function", font_size=32, color=GREEN, weight=BOLD).move_to(title_sig)
        eq_relu = MathTex(r"a = \max(0, z)", font_size=55, color=GREEN).next_to(title_relu, DOWN, buff=0.5)

        x_val.set_value(0)
        active_axes[0] = axes_relu
        active_func[0] = relu_func

        dead_zone = axes_relu.plot(relu_func, x_range=[-5, 0], color=RED, stroke_width=8)

        self.play(
            ReplacementTransform(axes_sig, axes_relu),
            ReplacementTransform(x_lbls_sig, x_lbls_relu),
            ReplacementTransform(y_lbls_sig, y_lbls_relu),
            ReplacementTransform(sig_curve, relu_curve),
            ReplacementTransform(flat_left, dead_zone),
            FadeOut(flat_right),
            Write(title_relu), Write(eq_relu),
            run_time=1.5
        )

        text_relu = Text(
            "Negative inputs are forced to hit the floor (Y=0).\nThe neuron dies.\nPositive inputs are unbounded.",
            font_size=24, color=WHITE, line_spacing=1.2
        ).next_to(eq_relu, DOWN, buff=0.8)

        self.play(Write(text_relu))

        self.play(x_val.animate.set_value(-4.5), run_time=2)
        self.wait(1)
        self.play(x_val.animate.set_value(4), run_time=3)
        self.wait(2)

        proj_group.clear_updaters()

        self.play(
            FadeOut(axes_relu), FadeOut(x_lbls_relu), FadeOut(y_lbls_relu),
            FadeOut(relu_curve), FadeOut(dead_zone), FadeOut(proj_group),
            FadeOut(title_relu), FadeOut(eq_relu), FadeOut(text_relu),
            run_time=1.5
        )

        conc_title = Text("CONCLUSION", font_size=36, weight=BOLD, color=YELLOW)
        conc_1 = Text("Activation functions force the linear space to bend.", font_size=30, color=WHITE)
        conc_2 = Text("Without this constraint, AI is just a basic calculator.", font_size=30, color=WHITE)

        conc_group = VGroup(conc_title, conc_1, conc_2).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Write(conc_group))
        self.wait(4.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
