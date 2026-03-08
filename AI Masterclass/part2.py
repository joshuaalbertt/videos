from manim import *
import numpy as np

class Part2Neuron(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        title = Text("PART 2: THE ANATOMY OF A NEURON", font_size=40, weight=BOLD).to_edge(UP, buff=0.5)

        inputs_abs = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(3)]).arrange(DOWN, buff=0.8).shift(LEFT * 4)
        neuron_abs = Circle(radius=0.8, color=WHITE).shift(LEFT * 0.5)

        labels_x = VGroup(*[MathTex(f"x_{i+1}", font_size=36).next_to(inputs_abs[i], LEFT, buff=0.3) for i in range(3)])
        lines = VGroup(*[Line(inputs_abs[i].get_right(), neuron_abs.get_left(), stroke_width=2) for i in range(3)])
        labels_w = VGroup(*[MathTex(f"w_{i+1}", font_size=30, color=YELLOW).move_to(lines[i].get_center() + UP * 0.3) for i in range(3)])

        eq_abs = MathTex("z = Wx + b", font_size=48).next_to(neuron_abs, RIGHT, buff=1)

        self.play(Write(title))
        self.wait(2)
        self.play(Create(inputs_abs), Write(labels_x))
        self.play(Create(lines), Write(labels_w), Create(neuron_abs))
        self.wait(10)
        self.play(Write(eq_abs))
        self.wait(10)

        diagram_abs = VGroup(title, inputs_abs, neuron_abs, labels_x, lines, labels_w, eq_abs)
        self.play(FadeOut(diagram_abs))
        self.wait(0.5)

        q_text = Text("How does it work?", font_size=40, weight=BOLD)
        self.play(Write(q_text))
        self.wait(1)
        self.play(q_text.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)

        ctx_title = Text("Case: Evaluating a Watch Purchase", font_size=36, color=BLUE)
        ctx_x1 = Text("x1 = Price", font_size=30)
        ctx_x2 = Text("x2 = Design", font_size=30)
        ctx_x3 = Text("x3 = Brand", font_size=30)

        ctx_group = VGroup(ctx_title, ctx_x1, ctx_x2, ctx_x3).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        self.play(Write(ctx_title))
        self.wait(5)
        self.play(FadeIn(ctx_x1, shift=RIGHT*0.5))
        self.play(FadeIn(ctx_x2, shift=RIGHT*0.5))
        self.play(FadeIn(ctx_x3, shift=RIGHT*0.5))
        self.wait(5)

        self.play(FadeOut(ctx_group))

        inputs = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(3)]).arrange(DOWN, buff=0.8).shift(LEFT * 4)
        neuron = Circle(radius=0.8, color=WHITE).shift(LEFT * 0.5)
        lbl_x = VGroup(*[MathTex(f"x_{i+1}", font_size=36).next_to(inputs[i], LEFT, buff=0.3) for i in range(3)])
        lns = VGroup(*[Line(inputs[i].get_right(), neuron.get_left(), stroke_width=2) for i in range(3)])
        lbl_w = VGroup(*[MathTex(f"w_{i+1}", font_size=30, color=YELLOW).move_to(lns[i].get_center() + UP * 0.3) for i in range(3)])

        diagram_re = VGroup(inputs, neuron, lbl_x, lns, lbl_w)
        self.play(FadeIn(diagram_re))
        self.wait(1)

        val_x1 = Text("Price (5)", font_size=24).next_to(inputs[0], LEFT, buff=0.3)
        val_x2 = Text("Design (8)", font_size=24).next_to(inputs[1], LEFT, buff=0.3)
        val_x3 = Text("Brand (2)", font_size=24).next_to(inputs[2], LEFT, buff=0.3)

        val_w1 = Text("-2", font_size=24, color=RED).move_to(lns[0].get_center() + UP * 0.3)
        val_w2 = Text("2", font_size=24, color=GREEN).move_to(lns[1].get_center() + UP * 0.3)
        val_w3 = Text("1", font_size=24, color=GREEN).move_to(lns[2].get_center() + UP * 0.3)

        val_b = Text("Bias (b) = -2", font_size=24, color=YELLOW).next_to(neuron, DOWN, buff=0.4)

        self.play(
            ReplacementTransform(lbl_x[0], val_x1),
            ReplacementTransform(lbl_w[0], val_w1)
        )
        self.play(
            ReplacementTransform(lbl_x[1], val_x2),
            ReplacementTransform(lbl_w[1], val_w2)
        )
        self.play(
            ReplacementTransform(lbl_x[2], val_x3),
            ReplacementTransform(lbl_w[2], val_w3)
        )
        self.play(Write(val_b))
        self.wait(1)

        eq_base = MathTex("z", "=", "(-2)(5) + (2)(8) + (1)(2) - 2", font_size=32).next_to(neuron, RIGHT, buff=1).shift(UP*0.5)
        eq_calc = MathTex("z", "=", "-10 + 16 + 2 - 2", font_size=32).next_to(eq_base, DOWN, aligned_edge=LEFT)
        eq_final = MathTex("z", "=", "6", font_size=48, color=YELLOW).next_to(eq_calc, DOWN, aligned_edge=LEFT)

        self.play(Write(eq_base))
        self.wait(0.5)
        self.play(Write(eq_calc))
        self.wait(0.5)
        self.play(Write(eq_final))
        self.wait(2)

        self.play(
            FadeOut(inputs), FadeOut(neuron), FadeOut(lns), FadeOut(val_b),
            FadeOut(val_x1), FadeOut(val_x2), FadeOut(val_x3),
            FadeOut(val_w1), FadeOut(val_w2), FadeOut(val_w3),
            FadeOut(eq_base), FadeOut(eq_calc), FadeOut(q_text)
        )
        self.play(eq_final.animate.to_corner(UR))

        q_act = Text("z = 6. What does this mean? We need a boundary.", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(q_act))
        self.wait(2)
        self.play(FadeOut(q_act))

        axes_sig = Axes(x_range=[-6, 6, 1], y_range=[-0.2, 1.2, 0.5], x_length=7, y_length=4).shift(LEFT * 3 + DOWN * 0.5)
        sig_graph = axes_sig.plot(lambda z: 1 / (1 + np.exp(-z)), color=PURPLE)

        sig_eq = MathTex("a = \\frac{1}{1 + e^{-z}}", font_size=40, color=PURPLE).next_to(axes_sig, UP)
        sig_name = Text("Sigmoid", font_size=32, color=PURPLE, weight=BOLD).next_to(sig_eq, UP)

        sig_desc_1 = Text("Forces output into the [0, 1] range", font_size=24).next_to(axes_sig, RIGHT, buff=1).shift(UP*0.5)
        sig_desc_2 = Text("Good for probability percentages.", font_size=24).next_to(sig_desc_1, DOWN, aligned_edge=LEFT)
        sig_desc_3 = Text("Limitation: AI is forced to cap at 1.\nHard to measure abstract intensity.", font_size=24, color=RED).next_to(sig_desc_2, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Create(axes_sig), Write(sig_name), Write(sig_eq))
        self.play(Create(sig_graph))
        self.play(Write(sig_desc_1), Write(sig_desc_2))
        self.wait(1.5)
        self.play(Write(sig_desc_3))
        self.wait(5)

        axes_relu = Axes(x_range=[-6, 6, 1], y_range=[-1, 6, 1], x_length=7, y_length=4).shift(LEFT * 3 + DOWN * 0.5)
        relu_graph = axes_relu.plot(lambda z: np.maximum(0, z), color=GREEN)

        relu_eq = MathTex("a = \\max(0, z)", font_size=40, color=GREEN).next_to(axes_relu, UP)
        relu_name = Text("ReLU (Rectified Linear Unit)", font_size=32, color=GREEN, weight=BOLD).next_to(relu_eq, UP)

        relu_desc_1 = Text("Negative values are forced to 0", font_size=24).next_to(axes_relu, RIGHT, buff=1).shift(UP*0.5)
        relu_desc_2 = Text("Positive values are left free", font_size=24).next_to(relu_desc_1, DOWN, aligned_edge=LEFT)
        relu_desc_3 = Text("Advantage: AI freely measures \nabstract scales without \na maximum limit.", font_size=24, color=GREEN).next_to(relu_desc_2, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(
            ReplacementTransform(axes_sig, axes_relu),
            ReplacementTransform(sig_graph, relu_graph),
            ReplacementTransform(sig_eq, relu_eq),
            ReplacementTransform(sig_name, relu_name),
            ReplacementTransform(sig_desc_1, relu_desc_1),
            ReplacementTransform(sig_desc_2, relu_desc_2),
            ReplacementTransform(sig_desc_3, relu_desc_3)
        )

        bend_point = Dot(axes_relu.c2p(0,0), color=YELLOW, radius=0.1)
        self.play(FadeIn(bend_point, scale=0.5))
        self.play(Wiggle(bend_point))
        self.wait(10)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
