from manim import *
import numpy as np

class Part5GradientDescent(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0A0A0A"
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        title = Text("PART 5: THE TRAINING LOOP", font_size=40, weight=BOLD).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        nodes_l1 = VGroup(*[Circle(radius=0.15, color=WHITE, stroke_width=2) for _ in range(3)]).arrange(DOWN, buff=0.5).shift(LEFT * 4)
        nodes_l2 = VGroup(*[Circle(radius=0.15, color=WHITE, stroke_width=2) for _ in range(4)]).arrange(DOWN, buff=0.5).shift(ORIGIN)
        nodes_l3 = VGroup(*[Circle(radius=0.15, color=WHITE, stroke_width=2) for _ in range(1)]).arrange(DOWN, buff=0.5).shift(RIGHT * 4)

        edges_1 = VGroup(*[Line(n1.get_right(), n2.get_left(), stroke_width=1.5, stroke_opacity=0.3, color=GREY_C) for n1 in nodes_l1 for n2 in nodes_l2])
        edges_2 = VGroup(*[Line(n1.get_right(), n2.get_left(), stroke_width=1.5, stroke_opacity=0.3, color=GREY_C) for n1 in nodes_l2 for n2 in nodes_l3])

        network = VGroup(edges_1, edges_2, nodes_l1, nodes_l2, nodes_l3)
        self.play(FadeIn(network, shift=UP*0.5))

        dots_1 = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in edges_1])
        for dot, edge in zip(dots_1, edges_1):
            dot.move_to(edge.get_start())

        self.play(*[MoveAlongPath(dot, edge) for dot, edge in zip(dots_1, edges_1)], run_time=1.5)
        self.play(FadeOut(dots_1), nodes_l2.animate.set_color(BLUE), run_time=0.5)

        dots_2 = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in edges_2])
        for dot, edge in zip(dots_2, edges_2):
            dot.move_to(edge.get_start())

        self.play(*[MoveAlongPath(dot, edge) for dot, edge in zip(dots_2, edges_2)], run_time=1.5)
        self.play(FadeOut(dots_2), nodes_l3.animate.set_color(RED), run_time=0.5)

        pred_text = MathTex(r"\hat{y} = 0.2", font_size=36, color=RED).next_to(nodes_l3, RIGHT, buff=0.5).shift(UP*0.3)
        actual_text = MathTex(r"y = 1.0", font_size=36, color=GREEN).next_to(nodes_l3, RIGHT, buff=0.5).shift(DOWN*0.3)

        self.play(Write(pred_text), Write(actual_text))
        self.wait(1)

        cost_eq = MathTex(r"C = (\hat{y} - y)^2", font_size=40).to_corner(DL).shift(UP*2 + RIGHT*1)
        cost_val = MathTex(r"C = (0.2 - 1.0)^2 = 0.64", font_size=40, color=RED).move_to(cost_eq, aligned_edge=LEFT)

        self.play(Write(cost_eq))
        self.wait(1.5)
        self.play(ReplacementTransform(cost_eq, cost_val))
        self.wait(1.5)

        total_cost = MathTex(r"J(\theta) = \sum (\hat{y}_i - y_i)^2", font_size=40).move_to(cost_val, aligned_edge=LEFT)
        self.play(ReplacementTransform(cost_val, total_cost))

        prob_text = Text("How do we minimize this error?", font_size=28, color=YELLOW).next_to(total_cost, UP, buff=0.5, aligned_edge=LEFT)
        self.play(Write(prob_text))
        self.wait(1)

        bp_text = Text("1. Chain Rule (Backprop): Find the blame.", font_size=24).next_to(total_cost, DOWN, buff=0.5, aligned_edge=LEFT)
        gd_text = Text("2. Gradient Descent: Take the step.", font_size=24).next_to(bp_text, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(bp_text))

        self.play(
            nodes_l3.animate.set_color(YELLOW),
            edges_2.animate.set_color(YELLOW).set_opacity(0.8),
            run_time=1.5
        )
        self.play(
            nodes_l2.animate.set_color(YELLOW),
            edges_1.animate.set_color(YELLOW).set_opacity(0.8),
            run_time=1.5
        )

        self.play(Write(gd_text))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=2)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[0, 16, 4],
            x_length=8,
            y_length=8,
            z_length=4,
            axis_config={"include_tip": False, "color": GREY_D}
        )
        self.play(Create(axes))

        surface = Surface(
            lambda u, v: axes.c2p(u, v, u**2 + v**2),
            u_range=[-3.5, 3.5],
            v_range=[-3.5, 3.5],
            checkerboard_colors=["#1E3A8A", "#0F172A"],
            resolution=(30, 30),
            fill_opacity=0.7,
            stroke_width=0.5,
            stroke_color=BLUE_E
        )
        self.play(Create(surface), run_time=2.5)

        self.move_camera(phi=15 * DEGREES, theta=45 * DEGREES, run_time=3)
        self.wait(1)

        self.move_camera(phi=65 * DEGREES, theta=-30 * DEGREES, zoom=1.3, run_time=3)
        self.wait(1)

        eq_grad = MathTex(r"\theta_{new} = \theta_{old} - \eta \nabla J", font_size=40, color=YELLOW).to_corner(UR)
        self.add_fixed_in_frame_mobjects(eq_grad)
        self.play(Write(eq_grad))

        w1_val = ValueTracker(2.5)
        w2_val = ValueTracker(2.5)

        ball = Dot3D(radius=0.15, color=YELLOW)

        def update_ball(m):
            w1 = w1_val.get_value()
            w2 = w2_val.get_value()
            z = w1**2 + w2**2
            m.move_to(axes.c2p(w1, w2, z))

        ball.add_updater(update_ball)
        self.play(FadeIn(ball))

        lbl_w1 = Text("w_1 :", font_size=28).to_corner(DL).shift(UP * 1.5 + RIGHT * 0.5)
        val_w1 = Text("2.5000", font_size=28, color=RED).next_to(lbl_w1, RIGHT)

        lbl_w2 = Text("w_2 :", font_size=28).next_to(lbl_w1, DOWN, aligned_edge=LEFT)
        val_w2 = Text("2.5000", font_size=28, color=RED).next_to(lbl_w2, RIGHT)

        lbl_loss = Text("Loss:", font_size=28).next_to(lbl_w2, DOWN, aligned_edge=LEFT)
        val_loss = Text(f"{2.5**2 + 2.5**2:.4f}", font_size=28, color=GREEN).next_to(lbl_loss, RIGHT)

        self.add_fixed_in_frame_mobjects(lbl_w1, val_w1, lbl_w2, val_w2, lbl_loss, val_loss)

        val_w1.add_updater(lambda m: m.become(Text(f"{w1_val.get_value():.4f}", font_size=28, color=RED).next_to(lbl_w1, RIGHT)))
        val_w2.add_updater(lambda m: m.become(Text(f"{w2_val.get_value():.4f}", font_size=28, color=RED).next_to(lbl_w2, RIGHT)))
        val_loss.add_updater(lambda m: m.become(Text(f"{w1_val.get_value()**2 + w2_val.get_value()**2:.4f}", font_size=28, color=GREEN).next_to(lbl_loss, RIGHT)))

        self.play(FadeIn(lbl_w1), FadeIn(val_w1), FadeIn(lbl_w2), FadeIn(val_w2), FadeIn(lbl_loss), FadeIn(val_loss))
        self.wait(1)

        learning_rate = 0.35

        for _ in range(3):
            cw1 = w1_val.get_value()
            cw2 = w2_val.get_value()

            grad_w1 = 2 * cw1
            grad_w2 = 2 * cw2

            nw1 = cw1 - learning_rate * grad_w1
            nw2 = cw2 - learning_rate * grad_w2

            start_pt = axes.c2p(cw1, cw2, cw1**2 + cw2**2)
            end_pt = axes.c2p(nw1, nw2, nw1**2 + nw2**2)

            arrow = Arrow3D(start=start_pt, end=end_pt, color=PINK, thickness=0.03)

            grad_label = Text("GRADIENT", font_size=24, color=PINK, weight=BOLD)
            grad_label.move_to(end_pt + UP * 0.8 + RIGHT * 0.5)
            grad_label.rotate(PI/2, RIGHT)
            grad_label.rotate(PI/4, OUT)

            self.play(Create(arrow), FadeIn(grad_label), run_time=1)
            self.wait(0.5)

            self.play(
                w1_val.animate.set_value(nw1),
                w2_val.animate.set_value(nw2),
                run_time=1.5,
                rate_func=smooth
            )

            self.play(FadeOut(arrow), FadeOut(grad_label), run_time=0.5)

        self.play(
            w1_val.animate.set_value(0),
            w2_val.animate.set_value(0),
            run_time=4,
            rate_func=linear
        )

        conv_bg = BackgroundRectangle(Text("GLOBAL MINIMUM REACHED", font_size=36), color=BLACK, fill_opacity=0.8, buff=0.2)
        conv_text = Text("GLOBAL MINIMUM REACHED", font_size=36, color=YELLOW, weight=BOLD)
        conv_group = VGroup(conv_bg, conv_text).to_edge(DOWN, buff=1)

        self.add_fixed_in_frame_mobjects(conv_group)
        self.play(FadeIn(conv_group, shift=UP*0.2))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
