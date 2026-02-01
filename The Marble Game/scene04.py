from manim import *

COLOR_SANGWOO = BLUE_E
COLOR_ALI = GREEN_E
COLOR_SIGNAL_NEUTRAL = WHITE
COLOR_SIGNAL_TRAP = RED
COLOR_TREE_PATH = GREY
COLOR_TEXT = WHITE

class BluffingSignaling(Scene):
    def construct(self):
        sangwoo = Circle(radius=0.5, color=COLOR_SANGWOO, fill_opacity=0.5).to_corner(UL).shift(DOWN*0.5, RIGHT*1)
        ali = Circle(radius=0.5, color=COLOR_ALI, fill_opacity=0.5).to_corner(UR).shift(DOWN*0.5, LEFT*1)

        label_s = Text("Sangwoo", font_size=20).next_to(sangwoo, DOWN)
        label_a = Text("Ali", font_size=20).next_to(ali, DOWN)

        self.play(
            FadeIn(sangwoo), FadeIn(label_s),
            FadeIn(ali), FadeIn(label_a),
            run_time=3
        )
        self.wait(6)

        signal = Circle(radius=0.15, color=COLOR_SIGNAL_NEUTRAL, fill_opacity=1)
        signal.move_to(sangwoo.get_center())

        self.play(Create(signal), run_time=1.5)

        self.play(
            signal.animate.move_to(ali.get_center()),
            run_time=4,
            rate_func=lambda t: t * (2 - t)
        )

        tree_origin = UP * 2
        root_node = Dot(point=tree_origin, color=COLOR_SIGNAL_NEUTRAL, radius=0.15)
        label_root = Text("Signal Received (s)", font_size=20).next_to(root_node, LEFT)

        self.play(
            TransformFromCopy(signal, root_node),
            Write(label_root),
            run_time=2
        )
        self.wait(3)

        mu_label = MathTex(r"\mu(s) = P(\text{Truth}|s)").scale(0.8).next_to(root_node, RIGHT, buff=0.5)

        bar_bg = Rectangle(height=1.0, width=0.3, color=WHITE).next_to(mu_label, RIGHT, buff=0.2)
        bar_fill = Rectangle(height=0.5, width=0.3, color=GREY, fill_opacity=0.8).move_to(bar_bg.get_bottom(), aligned_edge=DOWN)
        val_label = MathTex(r"0.5").scale(0.6).next_to(bar_bg, DOWN)

        self.play(Write(mu_label), Create(bar_bg), FadeIn(bar_fill), Write(val_label), run_time=2)

        bar_fill_high = Rectangle(height=0.99, width=0.3, color=GREEN, fill_opacity=0.8).move_to(bar_bg.get_bottom(), aligned_edge=DOWN)
        val_label_new = MathTex(r"0.99").scale(0.6).next_to(bar_bg, DOWN).set_color(GREEN)

        self.play(
            Transform(bar_fill, bar_fill_high),
            Transform(val_label, val_label_new),
            run_time=4
        )
        self.wait(2)

        left_branch_end = tree_origin + DOWN * 3 + LEFT * 3
        right_branch_end = tree_origin + DOWN * 3 + RIGHT * 3

        line_trust = Line(root_node.get_center(), left_branch_end, color=GREEN)
        line_verify = Line(root_node.get_center(), right_branch_end, color=GREY)

        node_trust = Dot(left_branch_end, color=GREEN, radius=0.15)
        node_verify = Dot(right_branch_end, color=GREY, radius=0.15)

        lbl_action_trust = Text("Trust", font_size=18).next_to(line_trust.get_center(), LEFT, buff=0.2).rotate(30*DEGREES)
        lbl_action_verify = Text("Verify", font_size=18).next_to(line_verify.get_center(), RIGHT, buff=0.2).rotate(-30*DEGREES)

        payoff_trust = MathTex(r"(Win, Win)").scale(0.7).next_to(node_trust, DOWN)
        payoff_verify = MathTex(r"(Safe, Safe)").scale(0.7).next_to(node_verify, DOWN)

        self.play(
            Create(line_trust), Create(line_verify),
            Create(node_trust), Create(node_verify),
            Write(lbl_action_trust), Write(lbl_action_verify),
            Write(payoff_trust), Write(payoff_verify),
            run_time=2
        )

        ali_token = ali.copy().scale(0.3).set_fill(opacity=1)
        self.play(ali_token.animate.move_to(root_node.get_center()), run_time=0.5)
        self.play(ali_token.animate.move_to(node_trust.get_center()), run_time=1.5)
        self.wait(0.5)
        self.play(signal.animate.set_color(COLOR_SIGNAL_TRAP), run_time=1)

        payoff_death = MathTex(r"(-\infty, Win)").scale(0.8).next_to(node_trust, DOWN).set_color(RED)

        trap_text = Text("FALSE SIGNAL!", color=RED, font_size=36, weight=BOLD).next_to(root_node, UP, buff=0.5)

        self.play(
            Transform(payoff_trust, payoff_death),
            node_trust.animate.scale(2).set_color(RED),
            line_trust.animate.set_color(RED),
            root_node.animate.set_color(RED),
            bar_fill.animate.set_color(RED),
            val_label.animate.set_color(RED),
            Flash(node_trust, color=RED, line_length=0.5, num_lines=10),
            Write(trap_text),
            run_time=3
        )

        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
