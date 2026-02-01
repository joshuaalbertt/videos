from manim import *
import random

class WhoIsBenford(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        title = Text("THE ORIGIN (1938)", font_size=40, weight=BOLD, color=GREY_A)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        book_cover = Rectangle(width=3.5, height=5, color=WHITE, fill_opacity=1, fill_color=GREY_C)
        book_cover.set_stroke(GREY_E, width=2)
        book_label = Text("LOGARITHM\nTABLES", font_size=24, color=BLACK, weight=BOLD)
        book_label.move_to(book_cover.get_center())

        closed_book = VGroup(book_cover, book_label)
        closed_book.move_to(ORIGIN)

        self.play(Write(title))
        self.play(
            closed_book.animate.shift(UP * 0),
            FadeIn(closed_book, shift=DOWN),
            run_time=2
        )
        self.wait(2)

        left_page = Rectangle(width=3.5, height=5, color=WHITE, fill_opacity=1, fill_color=GREY_B)
        left_page.set_stroke(GREY_D, width=1)
        left_page.shift(LEFT * 1.75)

        right_page = Rectangle(width=3.5, height=5, color=WHITE, fill_opacity=1, fill_color=GREY_B)
        right_page.set_stroke(GREY_D, width=1)
        right_page.shift(RIGHT * 1.75)

        left_content = VGroup()
        for i in range(12):
            line = Rectangle(width=2.5, height=0.08, fill_color=BLACK, fill_opacity=0.4, stroke_width=0)
            line.move_to(left_page.get_center() + UP * (1.5 - i * 0.25))
            left_content.add(line)

        right_content = VGroup()
        for i in range(12):
            line = Rectangle(width=2.5, height=0.08, fill_color=BLACK, fill_opacity=0.4, stroke_width=0)
            line.move_to(right_page.get_center() + UP * (1.5 - i * 0.25))
            right_content.add(line)

        page_1_label = Text("Page 1", font_size=20, color=BLACK)
        page_1_label.move_to(left_page.get_bottom() + UP * 0.3)

        page_9_label = Text("Page 9", font_size=20, color=BLACK)
        page_9_label.move_to(right_page.get_bottom() + UP * 0.3)

        opened_book_left = VGroup(left_page, left_content, page_1_label)
        opened_book_right = VGroup(right_page, right_content, page_9_label)

        self.remove(closed_book)
        self.add(closed_book)

        final_book_group = VGroup(opened_book_left, opened_book_right)

        self.play(
            ReplacementTransform(closed_book, opened_book_right),
            GrowFromEdge(opened_book_left, RIGHT),
            run_time=2
        )

        dirt_particles = VGroup()
        dirt_colors = [BLACK, GRAY_E, GRAY_D, "#5E4B35"]

        for _ in range(250):
            c = random.choice(dirt_colors)
            dot = Dot(radius=0.04, color=c)

            x_offset = random.uniform(-1.5, 1.5)
            y_offset = random.uniform(-2.2, 2.2)

            pos = left_page.get_center() + RIGHT * x_offset + UP * y_offset

            dot.move_to(pos)
            dot.set_opacity(random.uniform(0.1, 0.5))
            dirt_particles.add(dot)

        self.play(Create(dirt_particles), run_time=4)
        self.wait(1)

        insight_text = Text("Dirty = High Usage", font_size=36, color=YELLOW, weight=BOLD)
        insight_text.next_to(final_book_group, DOWN, buff=0.5)

        self.play(Write(insight_text), run_time=1.5)
        self.wait(4)

        self.play(
            FadeOut(final_book_group),
            FadeOut(dirt_particles),
            FadeOut(title),
            FadeOut(insight_text),
            run_time=1.5
        )
        self.wait(4)
