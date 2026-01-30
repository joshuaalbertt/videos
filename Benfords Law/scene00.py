from manim import *
import numpy as np

class BenfordLawHook(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        title = Text("BENFORD'S LAW", font_size=60, weight=BOLD)
        box = SurroundingRectangle(title, color=YELLOW, buff=0.3, stroke_width=4)
        title_group = VGroup(title, box).move_to(ORIGIN)

        self.add_fixed_in_frame_mobjects(title_group)
        self.play(Write(title), Create(box), run_time=1.5)

        self.wait(1)
        self.play(title_group.animate.to_corner(UR).scale(0.5), run_time=1.5)

        digits = range(1, 10)
        probabilities = [np.log10(1 + 1/d) for d in digits]

        axes = ThreeDAxes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 1],
            z_range=[0, 0.35, 0.1],
            x_length=8,
            y_length=2,
            z_length=5,
            axis_config={"include_tip": False, "stroke_width": 2}
        )

        x_labels = VGroup()
        for i in range(1, 10):
            pos = axes.c2p(i, -0.2, 0)
            label = Text(str(i), font_size=24).move_to(pos)
            label.rotate(90 * DEGREES, axis=RIGHT)
            x_labels.add(label)

        bars = VGroup()
        pct_labels = VGroup()

        for i, prob in enumerate(probabilities):
            digit = i + 1
            color = interpolate_color(RED_E, BLUE_E, i/8)
            bar_height = prob * (axes.z_length / 0.35)

            bar = Prism(dimensions=[0.6, 0.6, bar_height])
            bar.set_color(color)
            bar.set_opacity(0.9)
            bar.set_stroke(WHITE, width=1.5)
            pos = axes.c2p(digit, 0, prob/2)
            bar.move_to(pos)
            bars.add(bar)

            pct_val = prob * 100
            lbl = Text(f"{pct_val:.1f}%", font_size=18, weight=BOLD)
            top_point = bar.get_boundary_point(OUT)
            lbl.move_to(top_point + OUT * 0.4)
            lbl.rotate(90 * DEGREES, axis=RIGHT)
            pct_labels.add(lbl)

        chart_group = VGroup(axes, x_labels, bars, pct_labels)

        chart_group.move_to(ORIGIN).shift(DOWN * 1.5)

        self.play(Create(axes), Write(x_labels), run_time=1.5)

        self.play(
            LaggedStart(
                *[GrowFromPoint(bar, point=axes.c2p(i+1, 0, 0)) for i, bar in enumerate(bars)],
                lag_ratio=0.1
            ),
            run_time=5.0
        )

        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=2.5)

        self.play(
            LaggedStart(*[FadeIn(lbl, shift=UP*0.2) for lbl in pct_labels], lag_ratio=0.1),
            run_time=2
        )

        self.wait(4)

        self.play(
            FadeOut(chart_group),
            FadeOut(title_group),
            run_time=1.5
        )
