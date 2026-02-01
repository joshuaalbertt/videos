from manim import *
config.media_dir = "./manim_out"

class HilbertHotelInfiniteBus(Scene):
    def construct(self):
        rooms = VGroup()
        guests = VGroup()
        room_count = 8
        room_width = 1.2
        room_height = 1.8

        for i in range(room_count):
            room = Rectangle(width=room_width, height=room_height, color=WHITE, stroke_width=2)
            number = Text(str(i + 1), font_size=24).next_to(room, UP, buff=0.25)

            guest = Dot(radius=0.2, color=BLUE)
            guest.move_to(room.get_center())

            room_group = VGroup(room, number)
            rooms.add(room_group)
            guests.add(guest)

        rooms.arrange(RIGHT, buff=0)
        rooms.move_to(UP * 1.5)

        for i, guest in enumerate(guests):
            guest.move_to(rooms[i][0].get_center())

        ellipsis = Text("...", font_size=48).next_to(rooms, RIGHT, buff=0.5)

        scene_title = Text("SCENARIO 2: THE INFINITE BUS", font_size=32, weight=BOLD, color=GREY_B)
        scene_title.to_edge(UP, buff=0.4)

        self.play(Write(scene_title), run_time=1)
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

        problem_text = Text("Problem: Shifting +1 is not enough.", font_size=28, color=RED)
        problem_text.next_to(rooms, DOWN, buff=1.0)

        bus_body = Rectangle(width=6, height=1.5, color=YELLOW, fill_opacity=0.2)
        bus_wheels = VGroup(
            Circle(radius=0.25, color=WHITE, stroke_width=2).shift(LEFT * 2 + DOWN * 0.75),
            Circle(radius=0.25, color=WHITE, stroke_width=2).shift(RIGHT * 2 + DOWN * 0.75)
        )
        bus_text = Text("INFINITE BUS", font_size=24, color=YELLOW).move_to(bus_body)
        bus = VGroup(bus_body, bus_wheels, bus_text)

        target_bus_pos = problem_text.get_center() + DOWN * 2.0
        start_bus_pos = target_bus_pos + LEFT * 12
        bus.move_to(start_bus_pos)

        self.play(
            bus.animate.move_to(target_bus_pos),
            run_time=5,
            rate_func=rate_functions.ease_out_quint
        )
        self.play(Wiggle(bus, rotation_angle=0.01 * TAU), run_time=0.5)
        self.wait(0.5)

        self.play(Write(problem_text), run_time=3)
        self.wait(0.5)

        solution_text = MathTex(r"\text{Solution: Move } n \rightarrow 2n", color=BLUE, font_size=36)
        solution_text.move_to(problem_text)

        self.play(Transform(problem_text, solution_text), run_time=3)
        self.wait(0.5)

        arrows = VGroup()
        anims = []

        for i in range(room_count):
            current_room_idx = i
            target_room_idx = (i + 1) * 2 - 1

            start_point = rooms[current_room_idx][0].get_center()

            if target_room_idx < room_count:
                end_point = rooms[target_room_idx][0].get_center()
                if i < 3:
                    arrow = Arrow(start_point, end_point, buff=0.1, path_arc=-0.8, color=BLUE_A, stroke_width=2)
                    arrows.add(arrow)
                anims.append(guests[i].animate.move_to(end_point))
            else:
                anims.append(guests[i].animate.move_to(ellipsis).set_opacity(0))

        self.play(Create(arrows), run_time=1.5)

        self.play(
            *anims,
            FadeOut(arrows),
            run_time=2,
            rate_func=rate_functions.ease_in_out_sine
        )

        odd_rooms = VGroup()
        for i in range(0, room_count, 2):
            rect = SurroundingRectangle(rooms[i], color=GREEN, buff=0.05, stroke_width=3)
            odd_rooms.add(rect)

        open_text = Text("Odd rooms (1, 3, 5...) are open!", font_size=28, color=GREEN)
        open_text.move_to(solution_text)

        self.play(Create(odd_rooms), run_time=2)
        self.play(Transform(problem_text, open_text), run_time=1)
        self.wait(2)

        new_guests = VGroup()
        new_guest_anims = []

        for i in range(0, room_count, 2):
            g = Dot(radius=0.2, color=YELLOW)
            g.move_to(bus.get_center())
            new_guests.add(g)

            target = rooms[i][0].get_center()
            new_guest_anims.append(
                g.animate.move_to(target).set_path_arc(0.5)
            )

        self.add(new_guests)

        self.play(
            *new_guest_anims,
            FadeOut(odd_rooms),
            run_time=4,
            rate_func=rate_functions.ease_out_back
        )
        self.wait(1)

        final_eq = MathTex(r"\infty + \infty = \infty", font_size=80)
        final_eq.move_to(ORIGIN)

        self.play(
            FadeOut(problem_text),
            FadeOut(rooms),
            FadeOut(guests),
            FadeOut(new_guests),
            FadeOut(bus),
            FadeOut(ellipsis),
            FadeOut(scene_title),
            Write(final_eq),
            run_time=2.5
        )

        self.play(Indicate(final_eq, color=YELLOW, scale_factor=1.2), run_time=1.5)
        self.wait(4)
        self.play(FadeOut(Group(*self.mobjects)))
