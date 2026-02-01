from manim import *

COLOR_MARBLE = GOLD_E
COLOR_GRID = GREY_D
COLOR_BG = BLACK
COLOR_SQUID_PINK = "#ED1B76"

class ClosingScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.6)
        grid = NumberPlane(
            x_range=[-25, 25, 1],
            y_range=[-25, 25, 1],
            background_line_style={
                "stroke_color": COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }
        )
        grid.axes.set_stroke(color=COLOR_GRID, opacity=0.5)

        marble = Sphere(radius=0.4, color=COLOR_MARBLE, resolution=(24, 24))
        marble.set_sheen(0.8, direction=UL)
        marble.move_to(ORIGIN + OUT * 0.4)

        self.add(grid, marble)
        self.begin_ambient_camera_rotation(rate=0.08)
        self.move_camera(
            zoom=0.8,
            run_time=5
        )

        self.play(
            grid.background_lines.animate.set_stroke(opacity=0),
            grid.axes.animate.set_stroke(opacity=0),
            run_time=4
        )
        self.remove(grid)
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.move_camera(
            phi=80 * DEGREES,
            theta=-90 * DEGREES,
            zoom=1.2,
            run_time=2
        )

        qed_square = Square(side_length=1.5, fill_opacity=1, color=COLOR_SQUID_PINK)
        qed_square.set_stroke(width=0)

        text_qed = Text("Q.E.D.", font="serif", font_size=36, color=WHITE)
        text_qed.next_to(qed_square, UP, buff=0.2)

        text_desc = Text("Proof Complete", font="sans-serif", font_size=18, color=GREY)
        text_desc.next_to(qed_square, DOWN, buff=0.2)

        final_group = VGroup(qed_square, text_qed, text_desc)
        final_group.move_to(marble.get_center())

        final_group.rotate(90 * DEGREES, axis=RIGHT)

        self.play(
            ReplacementTransform(marble, qed_square),
            run_time=1.5
        )

        self.play(
            Write(text_qed),
            FadeIn(text_desc),
            run_time=2
        )

        self.wait(2)

        self.play(
            FadeOut(final_group),
            run_time=2
        )
        self.wait(1)
