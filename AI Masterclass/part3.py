from manim import *
import numpy as np

class Part3Network(Scene):
    def construct(self):
        self.camera.background_color = "#080808"

        title = Text("PART 3: DEEP NEURAL NETWORKS", font_size=40, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(title))

        premise_1 = Text("To produce complex outputs, a single neuron is never enough.", font_size=32, color=WHITE)
        premise_2 = Text("We need a massive, interconnected network.", font_size=32, color=YELLOW).next_to(premise_1, DOWN, buff=0.2)

        premise_group = VGroup(premise_1, premise_2).move_to(ORIGIN)
        self.play(Write(premise_1))
        self.play(FadeIn(premise_2, shift=UP*0.2))
        self.wait(2)
        self.play(FadeOut(premise_group))

        input_layer = VGroup(*[Circle(radius=0.15, color=BLUE, fill_opacity=0.8) for _ in range(4)]).arrange(DOWN, buff=0.4).shift(LEFT * 4.5)
        hidden_layer_1 = VGroup(*[Circle(radius=0.15, color=WHITE, fill_opacity=0.2, stroke_color=WHITE) for _ in range(5)]).arrange(DOWN, buff=0.3).shift(LEFT * 1.5)
        hidden_layer_2 = VGroup(*[Circle(radius=0.15, color=WHITE, fill_opacity=0.2, stroke_color=WHITE) for _ in range(5)]).arrange(DOWN, buff=0.3).shift(RIGHT * 1.5)
        output_layer = VGroup(*[Circle(radius=0.15, color=YELLOW, fill_opacity=0.8) for _ in range(2)]).arrange(DOWN, buff=0.5).shift(RIGHT * 4.5)

        all_lines = VGroup()
        layers = [input_layer, hidden_layer_1, hidden_layer_2, output_layer]

        for i in range(len(layers) - 1):
            for node1 in layers[i]:
                for node2 in layers[i+1]:
                    all_lines.add(Line(node1.get_right(), node2.get_left(), stroke_width=1.5, stroke_opacity=0.2, color=GREY_C))

        full_network = VGroup(all_lines, input_layer, hidden_layer_1, hidden_layer_2, output_layer)

        self.play(
            FadeIn(input_layer, shift=RIGHT*0.5),
            FadeIn(hidden_layer_1, shift=RIGHT*0.5),
            FadeIn(hidden_layer_2, shift=RIGHT*0.5),
            FadeIn(output_layer, shift=RIGHT*0.5),
            run_time=1.5
        )
        self.play(Create(all_lines, lag_ratio=0.1), run_time=2)
        self.wait(1)

        box_input = SurroundingRectangle(input_layer, color=BLUE, buff=0.3, stroke_width=3)
        lbl_input = Text("Input Layer", font_size=28, color=BLUE, weight=BOLD).next_to(box_input, UP)
        self.play(Create(box_input), Write(lbl_input))
        self.wait(1)
        self.play(FadeOut(box_input), FadeOut(lbl_input))

        hidden_group = VGroup(hidden_layer_1, hidden_layer_2)
        box_hidden = SurroundingRectangle(hidden_group, color=WHITE, buff=0.3, stroke_width=3)
        lbl_hidden = Text("Hidden Layers", font_size=28, color=WHITE, weight=BOLD).next_to(box_hidden, UP)
        self.play(Create(box_hidden), Write(lbl_hidden))
        self.wait(1)
        self.play(FadeOut(box_hidden), FadeOut(lbl_hidden))

        box_output = SurroundingRectangle(output_layer, color=YELLOW, buff=0.3, stroke_width=3)
        lbl_output = Text("Output Layer", font_size=28, color=YELLOW, weight=BOLD).next_to(box_output, UP)
        self.play(Create(box_output), Write(lbl_output))
        self.wait(1)
        self.play(FadeOut(box_output), FadeOut(lbl_output))

        self.play(full_network.animate.scale(0.55).to_edge(LEFT, buff=0.8))

        math_title = Text("From Nodes to Matrices", font_size=36, color=WHITE, weight=BOLD).shift(UP * 2.5 + RIGHT * 3)
        self.play(Write(math_title))

        eq_single_1 = MathTex("z_1 = w_{1,1}a_1 + w_{1,2}a_2 + \\dots + b_1", font_size=36).next_to(math_title, DOWN, buff=0.8)
        eq_single_2 = MathTex("z_2 = w_{2,1}a_1 + w_{2,2}a_2 + \\dots + b_2", font_size=36).next_to(eq_single_1, DOWN, buff=0.3)
        eq_dots = MathTex("\\vdots", font_size=36).next_to(eq_single_2, DOWN, buff=0.2)

        single_math_group = VGroup(eq_single_1, eq_single_2, eq_dots)

        note_single = Text("Calculating node-by-node is computationally impossible.", font_size=22, color=GREY_A).next_to(eq_dots, DOWN, buff=0.6)

        self.play(Write(single_math_group))
        self.play(FadeIn(note_single, shift=UP*0.2))
        self.wait(2)

        eq_matrix = MathTex("Z", "=", "W", "A", "+", "B", font_size=70).move_to(single_math_group)
        eq_matrix[0].set_color(YELLOW)
        eq_matrix[2].set_color(GREEN)
        eq_matrix[3].set_color(BLUE)

        self.play(
            ReplacementTransform(single_math_group, eq_matrix),
            FadeOut(note_single)
        )

        note_matrix_1 = Text("We explicitly force all weights into a single equation.", font_size=24, color=WHITE).next_to(eq_matrix, DOWN, buff=0.8)
        self.play(Write(note_matrix_1))
        self.play(FadeOut(math_title))
        self.wait(1)

        self.play(
            FadeOut(note_matrix_1),
            eq_matrix.animate.shift(UP * 1.5)
        )

        m_Z = Matrix([["z_1"], ["z_2"], ["\\vdots"]]).scale(0.6).set_color(YELLOW)
        m_eq = MathTex("=").scale(1.2)
        m_W = Matrix([["w_{1,1}", "w_{1,2}", "\\dots"], ["w_{2,1}", "w_{2,2}", "\\dots"], ["\\vdots", "\\vdots", "\\ddots"]]).scale(0.6).set_color(GREEN)
        m_A = Matrix([["a_1"], ["a_2"], ["\\vdots"]]).scale(0.6).set_color(BLUE)
        m_plus = MathTex("+").scale(1.2)
        m_B = Matrix([["b_1"], ["b_2"], ["\\vdots"]]).scale(0.6)

        full_matrix_group = VGroup(m_Z, m_eq, m_W, m_A, m_plus, m_B).arrange(RIGHT, buff=0.2).next_to(eq_matrix, DOWN, buff=1)

        self.play(
            ReplacementTransform(eq_matrix[0].copy(), m_Z),
            FadeIn(m_eq),
            ReplacementTransform(eq_matrix[2].copy(), m_W),
            ReplacementTransform(eq_matrix[3].copy(), m_A),
            FadeIn(m_plus),
            ReplacementTransform(eq_matrix[5].copy(), m_B)
        )
        self.wait(1)

        box_W = SurroundingRectangle(m_W, color=GREEN, buff=0.2, stroke_width=2)
        note_final = Text("Millions of parameters are forced \ninto this single 2D grid.", font_size=24, color=WHITE).next_to(full_matrix_group, DOWN, buff=0.8)

        self.play(Create(box_W), Write(note_final))
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
