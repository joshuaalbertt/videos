from manim import *
config.media_dir = "./manim_out"

class HilbertHotelHook(Scene):
    def construct(self):
        # --- STYLE CONFIGURATION ---
        # Using default sans-serif font for a clean look
        # Default background is black (fits the brand)

        # 1. HOTEL VISUALIZATION (Rooms 1, 2, 3, 4, 5, ...)
        # Create boxes representing rooms
        rooms = VGroup()
        room_count = 6
        room_width = 1.5
        room_height = 2.0

        for i in range(room_count):
            room = Rectangle(width=room_width, height=room_height, color=WHITE, stroke_width=2)
            # Add room number on top
            number = Text(str(i + 1), font_size=24).next_to(room, UP, buff=0.2)
            room_group = VGroup(room, number)
            rooms.add(room_group)

        # Arrange rooms horizontally
        rooms.arrange(RIGHT, buff=0)
        rooms.move_to(ORIGIN)

        # Add ellipsis (...) to indicate infinity
        ellipsis = Text("...", font_size=48).next_to(rooms, RIGHT, buff=0.5)

        # Hotel Title
        title = Text("HILBERT'S GRAND HOTEL", font_size=36, weight=BOLD)
        title.to_edge(UP, buff=1)

        # ANIMATION 1: Reveal Hotel
        # Dubbing: "Ini adalah hotel yang penuh..." (Santai)
        self.play(Write(title), run_time=1.5)
        self.play(
            LaggedStart(*[Create(room) for room in rooms], lag_ratio=0.15),
            Write(ellipsis),
            run_time=2.5
        )
        self.wait(0.5) # Pause for effect

        # NARRATION: "Every room is full."
        # Visual: Pop guests in with a satisfying 'pop' animation
        guests = VGroup()
        for i, room_group in enumerate(rooms):
            # Get the room box (first element of the group)
            box = room_group[0]
            guest = Dot(radius=0.3, color=BLUE) # Guest in Brand Color (Blue)
            guest.move_to(box.get_center())
            guests.add(guest)

        subtitle_1 = Text("Every single room is occupied.", font_size=24, slant=ITALIC).to_edge(DOWN, buff=1.5)

        self.play(
            LaggedStart(*[GrowFromCenter(guest) for guest in guests], lag_ratio=0.1),
            Write(subtitle_1),
            run_time=2
        )
        self.wait(1.5) # Give audience time to process "Full"

        # NARRATION: "NO VACANCY"
        # Visual: Make it flash slightly to emphasize the problem
        closed_sign = Text("NO VACANCY", color=RED, font_size=48, weight=BOLD)
        closed_sign.move_to(DOWN * 2) # Position below hotel

        self.play(FadeOut(subtitle_1))
        self.play(
            FadeIn(closed_sign, shift=UP * 0.5), # Slide up effect
            run_time=0.8
        )
        self.play(Indicate(closed_sign, color=RED_A)) # Flash effect
        self.wait(1.5) # Pause for dramatic tension

        # 2. THE PARADOX (Twist)
        # NARRATION: "But here is the paradox... Can we accept a new guest?"
        # Visual: 'NO VACANCY' transforms into the question

        paradox_text = Tex(r"\textbf{Can we still accept a new guest?}", color=YELLOW).to_edge(DOWN, buff=1.5)

        self.play(
            ReplacementTransform(closed_sign, paradox_text),
            run_time=1.5
        )
        self.wait(1)

        # NARRATION: "Even an infinite bus..."
        # Visual: Bus enters with a bit of "driving" motion (wiggling)
        bus_body = Rectangle(width=4, height=1.5, color=YELLOW, fill_opacity=0.2)
        bus_wheels = VGroup(
            Circle(radius=0.3, color=WHITE).shift(LEFT * 1.5 + DOWN * 0.75),
            Circle(radius=0.3, color=WHITE).shift(RIGHT * 1.5 + DOWN * 0.75)
        )
        bus_text = Text("INF BUS", font_size=24, color=YELLOW).move_to(bus_body)
        bus = VGroup(bus_body, bus_wheels, bus_text)
        bus.next_to(rooms, DOWN, buff=1.5).to_edge(LEFT)

        # Animate bus arriving
        self.play(
            FadeOut(paradox_text),
            bus.animate.move_to(DOWN * 2),
            run_time=2.5,
            rate_func=rush_into # Starts slow, speeds up
        )
        # Subtle wiggle to show it stopped
        self.play(Wiggle(bus, rotation_angle=0.01 * TAU), run_time=0.5)
        self.wait(1.5)

        # 3. CONCLUSION
        # NARRATION: "Infinity is not a number."
        # Visual: Clear everything for the final insight

        infinity_eq = MathTex(r"\infty \neq \text{Number}", font_size=72)
        infinity_eq.move_to(ORIGIN) # Center stage

        concept_text = Text("It is a concept.", font_size=32, color=GREY_A)
        concept_text.next_to(infinity_eq, DOWN, buff=0.5)

        # Clean up scene dramatically
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

        # Fade out all
        self.play(FadeOut(Group(*self.mobjects)))
