from manim import *
config.media_dir = "./manim_out"

class HilbertHotelOneGuest(Scene):
    def construct(self):
        rooms = VGroup()
        guests = VGroup()
        room_count = 6
        room_width = 1.5
        room_height = 2.0

        for i in range(room_count):
            room = Rectangle(width=room_width, height=room_height, color=WHITE, stroke_width=2)
            number = Text(str(i + 1), font_size=24).next_to(room, UP, buff=0.2)

            guest = Dot(radius=0.25, color=BLUE)
            guest.move_to(room.get_center())

            room_group = VGroup(room, number)
            rooms.add(room_group)
            guests.add(guest)

        rooms.arrange(RIGHT, buff=0)
        rooms.move_to(ORIGIN)

        for i, guest in enumerate(guests):
            guest.move_to(rooms[i][0].get_center())

        ellipsis = Text("...", font_size=48).next_to(rooms, RIGHT, buff=0.5)

        scene_title = Text("SCENARIO 1: THE NEW GUEST", font_size=32, weight=BOLD, color=GREY_B)
        scene_title.to_edge(UP, buff=0.8)

        self.play(Write(scene_title), run_time=1.5)
        self.play(
            LaggedStart(*[Create(r) for r in rooms], lag_ratio=0.1),
            Write(ellipsis),
            run_time=2
        )
        self.play(
            LaggedStart(*[GrowFromCenter(g) for g in guests], lag_ratio=0.1),
            run_time=1
        )
        self.wait(1)

        self.play(Indicate(guests, color=RED, scale_factor=1.1), run_time=2)
        self.wait(2)

        new_guest = Dot(radius=0.25, color=YELLOW)
        new_guest.move_to(rooms[0].get_center() + LEFT * 5 + DOWN * 0.5)

        guest_label = Text("Guest T", font_size=24, color=YELLOW).next_to(new_guest, UP, buff=0.2)
        new_guest_group = VGroup(new_guest, guest_label)

        problem_text = Text("One new guest arrives.", font_size=28)
        problem_text.next_to(rooms, DOWN, buff=1.2)

        self.play(
            new_guest_group.animate.next_to(rooms[0], LEFT, buff=1).set_y(rooms[0].get_y()),
            Write(problem_text),
            run_time=3,
            rate_func=rush_from
        )
        self.wait(1)

        solution_text = MathTex(r"\text{Solution: Shift } n \rightarrow n+1", color=BLUE)
        solution_text.move_to(problem_text)

        self.play(Transform(problem_text, solution_text), run_time=3)
        self.wait(1)

        arrows = VGroup()
        for i in range(room_count):
            start_point = rooms[i][0].get_center()
            if i < room_count - 1:
                end_point = rooms[i+1][0].get_center()
            else:
                end_point = ellipsis.get_center()

            arrow = Arrow(start_point, end_point, buff=0.3, path_arc=-0.6, color=YELLOW, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            arrows.add(arrow)

        self.play(Create(arrows), run_time=2.5)
        self.wait(0.5)

        anims = []
        for i in range(room_count):
            if i < room_count - 1:
                target = rooms[i+1][0].get_center()
                anims.append(guests[i].animate.move_to(target))
            else:
                anims.append(guests[i].animate.move_to(ellipsis).set_opacity(0))

        self.play(
            *anims,
            FadeOut(arrows),
            run_time=5,
            rate_func=smooth
        )
        self.wait(0.5)

        empty_room_indicator = SurroundingRectangle(rooms[0], color=GREEN, buff=0.1, stroke_width=4)
        open_text = Text("Room 1 is now empty!", font_size=28, color=GREEN)
        open_text.move_to(solution_text)

        self.play(Create(empty_room_indicator), run_time=1)
        self.play(Transform(problem_text, open_text), run_time=1)

        self.play(
            new_guest.animate.move_to(rooms[0][0].get_center()),
            FadeOut(guest_label),
            FadeOut(empty_room_indicator),
            run_time=3,
            rate_func=rate_functions.ease_out_cubic
        )
        self.wait(1)

        final_eq = MathTex(r"\infty + 1 = \infty", font_size=80)
        final_eq.move_to(ORIGIN)

        self.play(
            FadeOut(problem_text),
            FadeOut(rooms),
            FadeOut(guests),
            FadeOut(new_guest),
            FadeOut(ellipsis),
            FadeOut(scene_title),
            Write(final_eq),
            run_time=2.5
        )
        self.play(Indicate(final_eq, color=YELLOW, scale_factor=1.1), run_time=1)
        self.wait(5)
        self.play(FadeOut(Group(*self.mobjects)))
