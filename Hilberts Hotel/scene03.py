from manim import *
config.media_dir = "./manim_out"

class HilbertHotelConclusion(Scene):
    def construct(self):
        col_n = VGroup(*[MathTex(str(i), font_size=36) for i in range(1, 7)])
        col_n.add(MathTex(r"\vdots", font_size=36))
        col_n.arrange(DOWN, buff=0.5)
        col_n.move_to(LEFT * 2 + DOWN * 0.5)
        col_e = VGroup(*[MathTex(str(i*2), font_size=36) for i in range(1, 7)])
        col_e.add(MathTex(r"\vdots", font_size=36))
        col_e.arrange(DOWN, buff=0.5)
        col_e.move_to(RIGHT * 2 + DOWN * 0.5)

        header_n = MathTex(r"\mathbb{N}", color=BLUE).next_to(col_n, UP, buff=0.5)
        header_e = MathTex(r"\mathbb{E}", color=YELLOW).next_to(col_e, UP, buff=0.5)

        self.play(
            FadeIn(header_n), FadeIn(header_e),
            LaggedStart(*[Write(n) for n in col_n], lag_ratio=0.1),
            LaggedStart(*[Write(e) for e in col_e], lag_ratio=0.1),
            run_time=3
        )
        self.wait(1)

        mapping_text = Tex(r"Mapping ", r"Set", r" $\to$ ", r"Subset", font_size=36, color=GREY_A)
        mapping_text[1].set_color(BLUE)   
        mapping_text[3].set_color(YELLOW)
        mapping_text.to_edge(UP)

        self.play(Write(mapping_text), run_time=1.5)

        lines = VGroup()
        for i in range(6):
            l = Line(col_n[i].get_right(), col_e[i].get_left(), color=GREY)
            lines.add(l)

        self.play(
            Create(lines),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1)

        self.play(
            FadeOut(col_n), FadeOut(col_e), FadeOut(header_n), FadeOut(header_e),
            FadeOut(lines), FadeOut(mapping_text),
            run_time=1.5
        )

        aleph = MathTex(r"\aleph_0", font_size=144)
        aleph.set_color_by_gradient(BLUE, PURPLE)
        aleph.move_to(ORIGIN)
        label_aleph = Text("Cardinality of Infinite Sets", font_size=28, weight=LIGHT)
        label_aleph.next_to(aleph, DOWN, buff=0.5)

        self.play(DrawBorderThenFill(aleph), run_time=3)
        self.play(FadeIn(label_aleph, shift=UP*0.2), run_time=2)
        self.wait(2)

        self.play(
            aleph.animate.shift(UP * 1),
            FadeOut(label_aleph),
            run_time=1.5
        )

        question_text = Text("Are all infinities equal?", font_size=32, color=YELLOW)
        question_text.next_to(aleph, DOWN, buff=0.5)

        self.play(Write(question_text), run_time=2)
        self.wait(1)

        answer_text = Text("NO.", font_size=60, color=RED, weight=BOLD)
        answer_text.next_to(question_text, DOWN, buff=0.5)

        self.play(Indicate(question_text, color=WHITE), run_time=1)
        self.play(
            Write(answer_text),
            run_time=0.5
        )
        self.play(Indicate(answer_text, color=RED_A, scale_factor=1.2))
        self.wait(2)

        qed = MathTex(r"\text{Q.E.D.} \quad \blacksquare", font_size=48)
        qed.set_color(WHITE)
        qed.move_to(ORIGIN)

        self.play(
            FadeOut(aleph),
            FadeOut(question_text),
            FadeOut(answer_text),
            run_time=1
        )
        self.play(Write(qed), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(qed))
