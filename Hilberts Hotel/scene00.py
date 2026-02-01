from manim import *
config.media_dir = "./manim_out"

class HilbertHotelHook(Scene):
    def construct(self):
        rooms = VGroup()
        room_count = 6
        room_width = 1.5
        room_height = 2.0

        for i in range(room_count):
            room = Rectangle(width=room_width, height=room_height, color=WHITE, stroke_width=2)
            number = Text(str(i + 1), font_size=24).next_to(room, UP, buff=0.2)
            room_group = VGroup(room, number)
            rooms.add(room_group)

        rooms.arrange(RIGHT, buff=0)
        rooms.move_to(ORIGIN)
        ellipsis = Text("...", font_size=48).next_to(rooms, RIGHT, buff=0.5)
        title = Text("HILBERT'S GRAND HOTEL", font_size=36, weight=BOLD)
        title.to_edge(UP, buff=1)

        self.play(Write(title), run_time=1.5)
        self.play(
            LaggedStart(*[Create(room) for room in rooms], lag_ratio=0.15),
            Write(ellipsis),
            run_time=2.5
        )
        self.wait(0.5)

        guests = VGroup()
        for i, room_group in enumerate(rooms):
            box = room_group[0]
            guest = Dot(radius=0.3, color=BLUE)
            guest.move_to(box.get_center())
            guests.add(guest)

        subtitle_1 = Text("Every single room is occupied.", font_size=24, slant=ITALIC).to_edge(DOWN, buff=1.5)

        self.play(
            LaggedStart(*[GrowFromCenter(guest) for guest in guests], lag_ratio=0.1),
            Write(subtitle_1),
            run_time=2
        )
        self.wait(1.5)

        closed_sign = Text("NO VACANCY", color=RED, font_size=48, weight=BOLD)
        closed_sign.move_to(DOWN * 2)

        self.play(FadeOut(subtitle_1))
        self.play(
            FadeIn(closed_sign, shift=UP * 0.5),
            run_time=0.8
        )
        self.play(Indicate(closed_sign, color=RED_A))
        self.wait(1.5)

        paradox_text = Tex(r"\textbf{Can we still accept a new guest?}", color=YELLOW).to_edge(DOWN, buff=1.5)

        self.play(
            ReplacementTransform(closed_sign, paradox_text),
            run_time=1.5
        )
        self.wait(1)

        bus_body = Rectangle(width=4, height=1.5, color=YELLOW, fill_opacity=0.2)
        bus_wheels = VGroup(
            Circle(radius=0.3, color=WHITE).shift(LEFT * 1.5 + DOWN * 0.75),
            Circle(radius=0.3, color=WHITE).shift(RIGHT * 1.5 + DOWN * 0.75)
        )
        bus_text = Text("INF BUS", font_size=24, color=YELLOW).move_to(bus_body)
        bus = VGroup(bus_body, bus_wheels, bus_text)
        bus.next_to(rooms, DOWN, buff=1.5).to_edge(LEFT)

        self.play(
            FadeOut(paradox_text),
            bus.animate.move_to(DOWN * 2),
            run_time=2.5,
            rate_func=rush_into
        )

        self.play(Wiggle(bus, rotation_angle=0.01 * TAU), run_time=0.5)
        self.wait(1.5)

        infinity_eq = MathTex(r"\infty \neq \text{Number}", font_size=72)
        infinity_eq.move_to(ORIGIN)

        concept_text = Text("It is a concept.", font_size=32, color=GREY_A)
        concept_text.next_to(infinity_eq, DOWN, buff=0.5)

        self.play(
            FadeOut(title),
            FadeOut(bus),
            FadeOut(rooms),
            FadeOut(guests),
            FadeOut(ellipsis),
            run_time=1
        )

        self.play(Write(infinity_eq), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(concept_text, shift=UP * 0.2), run_time=1)
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
