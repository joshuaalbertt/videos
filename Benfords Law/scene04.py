from manim import *
import numpy as np

class BenfordFraudDetection(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        title = Text("THE APPLICATION", font_size=38, weight=BOLD)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.wait(2.5)

        self.play(title.animate.to_corner(UL).scale(0.7), run_time=1.5)

        records_data = ["1,492.50", "3,840.00", "1,105.20", "2,400.99", "1,980.00", "4,250.00", "1,320.75"]
        records_group = VGroup()

        for n in records_data:
            t_sym = Text("$ ", font_size=40, color=GREY_B)
            t_first = Text(n[0], font_size=40, color=YELLOW)
            t_rest = Text(n[1:], font_size=40, color=WHITE)
            row = VGroup(t_sym, t_first, t_rest).arrange(RIGHT, buff=0.1)
            records_group.add(row)

        records_group.arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(LaggedStart(*[Write(row) for row in records_group], lag_ratio=0.3), run_time=2.5)

        self.wait(1.5)

        self.play(
            *[row[0].animate.set_opacity(0.1) for row in records_group],
            *[row[2].animate.set_opacity(0.1) for row in records_group],
            run_time=1
        )
        self.wait(0.5)

        first_digits = VGroup()
        for row in records_group:
            digit_copy = row[1].copy()
            first_digits.add(digit_copy)

        self.play(
            FadeOut(records_group),
            first_digits.animate.arrange(RIGHT, buff=0.3).move_to(ORIGIN),
            run_time=1.5
        )

        self.wait(2)

        self.play(FadeOut(first_digits), run_time=0.5)

        self.play(title.animate.to_edge(RIGHT).scale(1), run_time=1)

        self.wait(1)

        axes = ThreeDAxes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 1],
            z_range=[0, 0.4, 0.1],
            x_length=9,
            y_length=2,
            z_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN * 3 + LEFT * 0.5)

        x_labels = VGroup()
        for i in range(1, 10):
            label = Text(str(i), font_size=24).move_to(axes.c2p(i, -0.3, 0))
            label.rotate(90 * DEGREES, axis=RIGHT)
            label.rotate(45 * DEGREES, axis=OUT)
            x_labels.add(label)

        self.play(Create(axes), Write(x_labels), run_time=1.5)

        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=2.5)

        curve_points = [axes.c2p(t, 0, np.log10(1 + 1/t)) for t in np.linspace(1, 9, 50)]
        curve = VMobject().set_points_smoothly(curve_points).set_color(YELLOW).set_stroke(width=5)

        self.play(Create(curve), run_time=1.5)

        benford_probs = [np.log10(1 + 1/d) for d in range(1, 10)]
        real_bars = VGroup()

        for i, prob in enumerate(benford_probs):
            bar = Prism(dimensions=[0.5, 0.5, prob * 10])
            bar.set_color(GREEN)
            bar.set_opacity(0.8)
            bar.move_to(axes.c2p(i+1, 0, prob/2))
            real_bars.add(bar)

        status_real = Text("AUTHENTIC RECORDS", font_size=30, color=GREEN, weight=BOLD)
        status_real.to_edge(RIGHT)
        self.add_fixed_in_frame_mobjects(status_real)

        self.play(Write(status_real))

        self.play(
            LaggedStart(
                *[GrowFromPoint(bar, point=axes.c2p(i+1, 0, 0)) for i, bar in enumerate(real_bars)],
                lag_ratio=0.1
            ),
            run_time=2.5
        )

        self.wait(2.5)

        fake_probs = [0.12, 0.10, 0.09, 0.08, 0.18, 0.17, 0.12, 0.08, 0.06]
        fake_bars = VGroup()

        for i, prob in enumerate(fake_probs):
            color = RED if prob > benford_probs[i] + 0.02 else GREY_D
            bar = Prism(dimensions=[0.5, 0.5, prob * 10])
            bar.set_color(color)
            bar.set_opacity(0.9)
            bar.move_to(axes.c2p(i+1, 0, prob/2))
            fake_bars.add(bar)

        status_fake = Text("FRAUD DETECTED!", font_size=36, color=RED, weight=BOLD)
        status_fake.to_edge(RIGHT)
        self.add_fixed_in_frame_mobjects(status_fake)

        self.play(
            ReplacementTransform(status_real, status_fake),
            Transform(real_bars, fake_bars),
            run_time=2
        )

        self.wait(3)

        self.play(
            real_bars[4].animate.set_color(PURE_RED),
            real_bars[5].animate.set_color(PURE_RED),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.play(
            real_bars[4].animate.set_color(PURE_RED),
            real_bars[5].animate.set_color(PURE_RED),
            rate_func=there_and_back,
            run_time=1.5
        )

        self.wait(4.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.5
        )
        self.wait(2)
