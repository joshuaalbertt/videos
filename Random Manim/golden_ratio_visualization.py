from manim import *

class GoldenSpiralPolished(MovingCameraScene):
    def construct(self):
        fib_series = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        colors = [TEAL_D, TEAL_C, BLUE_D, BLUE_C, PURPLE_D, PURPLE_C, MAROON_D, RED_C, ORANGE]

        full_spiral_group = VGroup()
        squares_group = VGroup()
        arcs_group = VGroup()
        title = Text("Golden Ratio", font_size=48)
        title.set_color_by_gradient(BLUE, GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        prev_square = None
        direction_vectors = [RIGHT, UP, LEFT, DOWN]
        alignment_directions = [DOWN, RIGHT, UP, LEFT]

        for i, n in enumerate(fib_series):
            color_fill = colors[i % len(colors)]
            color_stroke = color_fill.lighter(0.5)
            square = Square(side_length=n)
            square.set_fill(color_fill, opacity=0.3)
            square.set_stroke(color_stroke, width=2)
            if prev_square is not None:
                curr_dir = direction_vectors[i % 4]
                square.next_to(prev_square, curr_dir, buff=0)

                align_dir = alignment_directions[i % 4]
                square.align_to(prev_square, align_dir)
            else:
                square.move_to(ORIGIN)

            font_scale = 0.4 * n if n < 3 else 0.8
            label = Text(str(n), font="Arial", weight=BOLD).scale(font_scale)
            label.move_to(square.get_center())
            label.set_color(WHITE)
            start_angle = (i * PI / 2) + PI

            arc = Arc(
                radius=n,
                angle=PI / 2,
                start_angle=start_angle,
                arc_center=self.get_arc_center(square, i),
                color=GOLD_E,
                stroke_width=6
            )

            arc.set_sheen(0.2, direction=UR)
            square_w_label = VGroup(square, label)
            squares_group.add(square_w_label)
            arcs_group.add(arc)
            full_spiral_group.add(square_w_label, arc)
            prev_square = square

        full_spiral_group.move_to(ORIGIN)
        self.camera.frame.scale(0.5)
        self.camera.frame.move_to(squares_group[0])

        for i in range(len(fib_series)):
            square_obj = squares_group[i][0]
            label_obj = squares_group[i][1]
            arc_obj = arcs_group[i]

            self.play(
                GrowFromCenter(square_obj),
                Write(label_obj),
                self.camera.frame.animate.move_to(square_obj).scale(1.15),
                run_time=0.8,
                rate_func=smooth
            )
            self.play(Create(arc_obj), run_time=0.5, rate_func=smooth)

        self.wait(0.5)

        phi_text = Text("Phi ≈ 1.61803...", color=GOLD, font="Arial").scale(1.2)
        phi_text.next_to(full_spiral_group, DOWN, buff=1)

        self.play(
            self.camera.frame.animate.scale_to_fit_height(full_spiral_group.height * 1.4).move_to(full_spiral_group),
            Write(phi_text),
            run_time=2
        )

        self.play(arcs_group.animate.set_stroke(GOLD_A, width=8, opacity=1), run_time=1.5)
        self.wait(3)

    def get_arc_center(self, square, index):
        corners = [
            square.get_corner(DL),
            square.get_corner(DR),
            square.get_corner(UR),
            square.get_corner(UL),
        ]
        return corners[index % 4]
