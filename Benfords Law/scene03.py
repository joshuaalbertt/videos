from manim import *
import random

class BenfordExceptions(Scene):
    def construct(self):
        title_fail = Text("WHEN DOES IT FAIL?", font_size=40, color=RED).to_corner(UL)
        self.play(Write(title_fail))

        balls = VGroup()
        for i in range(5):
            circle = Circle(radius=0.5, color=WHITE, fill_opacity=0, stroke_width=2)
            num = Integer(random.randint(10, 99), color=WHITE)
            ball = VGroup(circle, num).shift(LEFT * 3 + RIGHT * i * 1.5)
            balls.add(ball)

        balls.move_to(UP * 1)

        axes_lottery = Axes(
            x_range=[0, 10, 1], y_range=[0, 20, 10],
            x_length=6, y_length=2,
            axis_config={"include_tip": False}
        ).shift(DOWN * 1.5)

        bars_lottery = VGroup()
        for i in range(1, 10):
            rect = Rectangle(width=0.4, height=1.5, color=BLUE, fill_opacity=0.8)
            rect.move_to(axes_lottery.c2p(i, 10))
            bars_lottery.add(rect)

        label_lottery = Text("Uniform Distribution (Lottery)", font_size=24, color=BLUE)
        label_lottery.next_to(bars_lottery, UP)

        self.play(LaggedStart(*[FadeIn(b, scale=0.5) for b in balls], lag_ratio=0.1))
        self.play(Create(axes_lottery), FadeIn(bars_lottery), Write(label_lottery))

        fail_stamp = Text("VIOLATION", font_size=60, color=RED, weight=BOLD).rotate(15*DEGREES)
        fail_stamp.set_opacity(0.8)
        self.play(FadeIn(fail_stamp, scale=2), run_time=0.5)
        self.wait(2)

        self.play(
            FadeOut(balls), FadeOut(axes_lottery), FadeOut(bars_lottery),
            FadeOut(label_lottery), FadeOut(fail_stamp)
        )

        height_text = Text("Human Height: 160cm - 190cm", font_size=30, color=WHITE).shift(UP * 1)

        axes_height = Axes(
            x_range=[0, 10, 1], y_range=[0, 100, 50],
            x_length=6, y_length=2,
            axis_config={"include_tip": False}
        ).shift(DOWN * 1)

        bar_1 = Rectangle(width=0.4, height=2, color=RED, fill_opacity=0.8)
        bar_1.move_to(axes_height.c2p(1, 50))

        label_height = Text("Constrained Range", font_size=24, color=RED)
        label_height.next_to(axes_height, UP, buff=2.5)

        self.play(Write(height_text))
        self.play(Create(axes_height), GrowFromEdge(bar_1, DOWN), Write(label_height))

        fail_stamp_2 = Text("VIOLATION", font_size=60, color=RED, weight=BOLD).rotate(15*DEGREES)
        self.play(FadeIn(fail_stamp_2, scale=2), run_time=0.5)
        self.wait(2)

        self.play(
            FadeOut(height_text), FadeOut(axes_height), FadeOut(bar_1),
            FadeOut(label_height), FadeOut(fail_stamp_2),
            FadeOut(title_fail)
        )

        title_rule = Text("THE REQUIREMENT", font_size=40, color=GREEN).to_corner(UL)
        self.play(Write(title_rule))

        number_line = NumberLine(
            x_range=[0, 10000, 1000],
            length=10,
            include_numbers=True,
            font_size=20
        )

        orders_text = Text("Orders of Magnitude", font_size=36, color=YELLOW)
        orders_text.shift(UP * 2)

        scale_10 = Text("Range: 1 - 10", font_size=24).next_to(number_line, UP)
        scale_100 = Text("Range: 1 - 100", font_size=24).next_to(number_line, UP)
        scale_1000 = Text("Range: 1 - 1,000", font_size=24).next_to(number_line, UP)
        scale_10000 = Text("Range: 1 - 10,000+", font_size=24).next_to(number_line, UP)

        self.play(Create(number_line), Write(orders_text))

        self.play(Transform(scale_10, scale_100))
        self.play(number_line.animate.scale(0.8), run_time=0.5)

        self.play(Transform(scale_10, scale_1000))
        self.play(number_line.animate.scale(0.8), run_time=0.5)

        self.play(Transform(scale_10, scale_10000))
        self.play(number_line.animate.scale(0.8), run_time=0.5)

        check_mark = Text("✔ WORKS", font_size=50, color=GREEN, weight=BOLD).shift(DOWN * 2)
        self.play(Write(check_mark))

        self.wait(3)

        self.play(
            FadeOut(number_line), FadeOut(orders_text),
            FadeOut(scale_10), FadeOut(check_mark), FadeOut(title_rule),
            run_time=1.5
        )
        self.wait(2)
