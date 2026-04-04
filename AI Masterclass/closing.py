from manim import *

class OutroScene(Scene):
    def construct(self):
        self.camera.background_color = "#0A0A0A"

        title = Text("THE ANATOMY OF AI", font_size=40, weight=BOLD, color=YELLOW).to_edge(UP, buff=1)
        self.play(Write(title))

        eq_1 = MathTex(r"1.\text{ Structure: } Z = WX + B", font_size=36, color=WHITE)
        eq_2 = MathTex(r"2.\text{ Logic: } A = \max(0, Z)", font_size=36, color=GREEN)
        eq_3 = MathTex(r"3.\text{ Error: } L = \frac{1}{2}\sum(\hat{y} - y)^2", font_size=36, color=RED)
        eq_4 = MathTex(r"4.\text{ Learning: } \theta_{new} = \theta_{old} - \eta \nabla L", font_size=36, color=BLUE)

        summary_group = VGroup(eq_1, eq_2, eq_3, eq_4).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(ORIGIN)

        self.play(Write(eq_1), run_time=3)
        self.play(Write(eq_2), run_time=3)
        self.play(Write(eq_3), run_time=3)
        self.play(Write(eq_4), run_time=3)
        self.wait(4)

        self.play(
            FadeOut(title),
            FadeOut(summary_group),
            run_time=1.5
        )

        thesis_1 = Text("There is no magic.", font_size=48, color=GREY_B)
        thesis_2 = Text("Only mathematics.", font_size=48, weight=BOLD, color=WHITE).next_to(thesis_1, DOWN, buff=0.2)

        thesis_group = VGroup(thesis_1, thesis_2).move_to(ORIGIN)

        self.play(FadeIn(thesis_1, shift=UP*0.2))
        self.wait(0.5)
        self.play(FadeIn(thesis_2, shift=UP*0.2))
        self.wait(2)

        self.play(FadeOut(thesis_group))
