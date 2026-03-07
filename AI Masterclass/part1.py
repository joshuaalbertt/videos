from manim import *

class Part1Philosophy(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        title = Text("PART 1: THE PHILOSOPHY", font_size=40, color=GREY_A, weight=BOLD).to_edge(UP)
        self.play(Write(title))
        self.wait(4)

        eq_base = MathTex("f(", "\\text{Input}", ") = ", "\\text{Output}", font_size=60)
        eq_base.set_color_by_tex("Input", BLUE)
        eq_base.set_color_by_tex("Output", GREEN)

        self.play(Write(eq_base))
        self.wait(4)

        eq_math = MathTex("f(", "x", ") = ", "y", font_size=60)
        eq_math.set_color_by_tex("x", BLUE)
        eq_math.set_color_by_tex("y", GREEN)

        self.play(ReplacementTransform(eq_base, eq_math))

        subtitle = Text("AI is just finding the right function.", font_size=30, color=YELLOW).next_to(eq_math, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=DOWN * 0.5))
        self.wait(4)

        self.play(FadeOut(eq_math), FadeOut(subtitle))

        uat_title = Text("Universal Approximation Theorem", font_size=36, color=WHITE).next_to(title, DOWN, buff=0.2)
        self.play(Write(uat_title))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN * 0.5)

        self.play(Create(axes))

        target_curve = axes.plot(lambda x: np.sin(x) + 0.5 * np.cos(2 * x), color=GREEN, stroke_width=4)
        target_label = Text("Target Function (Reality)", font_size=24, color=GREEN).next_to(target_curve, UP, buff=0.5)

        self.play(Create(target_curve), Write(target_label))
        self.wait(4)

        approx_label = Text("Neural Network Approximation", font_size=24, color=BLUE).move_to(target_label)

        steps = [3, 8, 15, 30]
        prev_approx = None

        self.play(ReplacementTransform(target_label, approx_label))

        for n in steps:
            x_vals = np.linspace(0, 10, n)
            y_vals = [np.sin(x) + 0.5 * np.cos(2 * x) for x in x_vals]

            approx_points = [axes.c2p(x, y) for x, y in zip(x_vals, y_vals)]
            approx_curve = VMobject(stroke_color=BLUE, stroke_width=4).set_points_as_corners(approx_points)

            neuron_text = Text(f"Neurons: {n}", font_size=24, color=YELLOW).next_to(axes, DOWN)

            if prev_approx is None:
                self.play(Create(approx_curve), FadeIn(neuron_text), run_time=1)
                prev_approx = approx_curve
                prev_text = neuron_text
            else:
                self.play(
                    ReplacementTransform(prev_approx, approx_curve),
                    ReplacementTransform(prev_text, neuron_text),
                    run_time=1
                )
                prev_approx = approx_curve
                prev_text = neuron_text

            self.wait(0.5)

        self.wait(1)

        insight = Text("Enough simple functions can build ANY complex shape.", font_size=28, color=YELLOW).next_to(axes, DOWN, buff=0.5)
        self.play(
            FadeOut(prev_text),
            Write(insight)
        )
        self.wait(10)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
