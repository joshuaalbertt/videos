from manim import *
import random

COLOR_MARBLE = GOLD_E
COLOR_FLOOR = "#2C2C2C"
COLOR_SQUID_PINK = "#ED1B76"
COLOR_SQUID_GREEN = "#037A68"
COLOR_TITLE = WHITE

class HookScene(ThreeDScene):
    def construct(self):
        self.camera.set_phi(60 * DEGREES)
        self.camera.set_theta(-45 * DEGREES)
        self.camera.set_zoom(0.8)

        floor_plane = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-10, 10, 1],
            background_line_style={"stroke_color": GREY_D, "stroke_opacity": 0.2}
        ).rotate(0, axis=RIGHT)

        sand_particles = VGroup()
        for _ in range(100):
            d = Dot(point=[random.uniform(-6,6), random.uniform(-4,4), 0], radius=0.03, color=GREY_B, fill_opacity=random.uniform(0.2, 0.6))
            sand_particles.add(d)

        floor_group = VGroup(floor_plane, sand_particles)

        triangle = Triangle(color=COLOR_SQUID_PINK, stroke_width=2).scale(2).move_to(LEFT*3 + UP*2).set_opacity(0.3)
        square = Square(color=COLOR_SQUID_PINK, stroke_width=2).scale(1.5).move_to(RIGHT*3 + DOWN*1).set_opacity(0.3)
        circle_shape = Circle(color=COLOR_SQUID_PINK, stroke_width=2).scale(1.5).move_to(LEFT*2 + DOWN*3).set_opacity(0.3)
        bg_symbols = VGroup(triangle, square, circle_shape)

        self.add(floor_group, bg_symbols)

        marble = Sphere(radius=0.3, color=COLOR_MARBLE, resolution=(16, 16))
        marble.set_sheen(0.5, direction=UL)

        start_pos = OUT * 4
        marble.move_to(np.array([0, 0, 5]))
        self.add(marble)

        target_pos = np.array([0, 0, 0.3])

        self.move_camera(
            zoom=1.2,
            added_anims=[marble.animate.move_to(target_pos)],
            run_time=0.8,
            rate_func=rate_functions.ease_in_cubic
        )

        ripple = Circle(radius=0.5, color=WHITE, stroke_width=2).rotate(0)
        ripple.set_stroke(opacity=0.8)
        self.play(
            Create(ripple),
            ripple.animate.scale(3).set_stroke(opacity=0),
            marble.animate.shift(np.array([0, 0, 0.5])).set_rate_func(rate_functions.ease_out_quad),
            run_time=0.4
        )
        self.remove(ripple)

        self.play(
            marble.animate.move_to(target_pos),
            run_time=0.3,
            rate_func=rate_functions.ease_in_quad
        )

        self.move_camera(
            phi=45*DEGREES,
            theta=-10*DEGREES,
            run_time=5
        )

        black_rect = Rectangle(width=20, height=20, color=BLACK, fill_opacity=1)
        self.add_fixed_in_frame_mobjects(black_rect)
        self.play(FadeIn(black_rect), run_time=1)

        title_main = Text("THE MARBLE GAME", font_size=72, color=WHITE, font="serif")
        title_sub = Text("SQUID GAME EPISODE 6", font_size=24, color=GREY, font="sans-serif")

        symbols_final = VGroup(
            Triangle().scale(0.5), Square().scale(0.5), Circle().scale(0.5)
        ).arrange(RIGHT, buff=0.8).set_color(COLOR_SQUID_PINK)

        final_group = VGroup(title_main, title_sub, symbols_final)
        final_group.arrange(DOWN, buff=0.5)
        final_group.move_to(ORIGIN)

        self.add_fixed_in_frame_mobjects(final_group)

        self.play(
            DrawBorderThenFill(title_main),
            FadeIn(title_sub, shift=UP * 0.2),
            LaggedStart(*[Create(s) for s in symbols_final], lag_ratio=0.15),
            run_time=2.5
        )

        self.wait(2)

        self.play(FadeOut(final_group), run_time=1.5)
