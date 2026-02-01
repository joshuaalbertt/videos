from manim import *

class Scene02(Scene):
    def construct(self):
        title = Text("INFORMATION ASYMMETRY", font_size=36, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        matrix_data = [
            ["W/L", "L/W"],
            ["L/W", "W/L"]
        ]

        row_labels = [Text("Odd", font_size=24), Text("Even", font_size=24)]
        col_labels = [Text("Odd", font_size=24), Text("Even", font_size=24)]

        payoff_table = Table(
            matrix_data,
            row_labels=row_labels,
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": WHITE},
            element_to_mobject_config={"font_size": 24}
        ).scale(0.7)

        player_a_label = Text("Player A", font_size=28, color=BLUE).next_to(payoff_table, UP)
        player_b_label = Text("Player B", font_size=28, color=RED).next_to(payoff_table, LEFT).rotate(PI/2)

        self.play(
            Create(payoff_table),
            Write(player_a_label),
            Write(player_b_label)
        )
        self.wait(1)

        cell_1 = payoff_table.get_cell((1,1))
        cell_2 = payoff_table.get_cell((2,2))

        highlight_box = SurroundingRectangle(cell_1, color=YELLOW, buff=0.1)

        self.play(Create(highlight_box))
        self.wait(10)
        self.play(Transform(highlight_box, SurroundingRectangle(cell_2, color=YELLOW, buff=0.1)))
        self.wait(10)

        bayesian_text = Tex(r"Bayesian Game: \\ Beliefs vs Strategies", color=YELLOW, font_size=32)
        bayesian_text.to_corner(DR)
        self.play(Write(bayesian_text))
        self.wait(6)

        self.play(
            FadeOut(payoff_table),
            FadeOut(player_a_label),
            FadeOut(player_b_label),
            FadeOut(highlight_box),
            FadeOut(bayesian_text)
        )

        prob_text = MathTex(r"P(\text{Correct}) = 0.5", font_size=48)
        prob_text.shift(UP*2)
        self.play(Write(prob_text), run_time = 1.5)

        chart = VGroup()
        sector_fail = Sector(radius=1.5, start_angle=0, angle=PI, color=RED, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)
        sector_win = Sector(radius=1.5, start_angle=PI, angle=PI, color=GREEN, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)

        chart.add(sector_fail, sector_win)
        chart.next_to(prob_text, DOWN)

        lbl_random = Text("Random", font_size=24).move_to(chart.get_center())

        self.play(Create(chart), run_time=1.3)
        self.play(Write(lbl_random), run_time=1.5)
        self.wait(1)

        reality_text = Text("Only true if purely random!", color=RED, font_size=28).next_to(chart, DOWN)
        self.play(Write(reality_text))
        self.wait(0.9)

        self.play(FadeOut(prob_text), FadeOut(chart), FadeOut(reality_text), FadeOut(lbl_random))

        pattern_title = Text("Human Pattern Analysis", font_size=32).to_edge(UP)
        self.play(Transform(title, pattern_title))

        def get_marbles(count, color=WHITE):
            marbles = VGroup()
            for i in range(count):
                m = Circle(radius=0.15, color=color, fill_opacity=0.8)
                m.move_to(DOWN * 2 + UP * i * 0.35)
                marbles.add(m)
            return marbles

        counts_random = [3, 5, 2, 7, 1]

        label_state = Text("State: Random", color=GREEN, font_size=36).next_to(title, DOWN)
        self.play(Write(label_state))

        for count in counts_random:
            new_stack = get_marbles(count, color=BLUE)
            self.add(new_stack)
            self.wait(0.4)
            self.remove(new_stack)

        self.play(Transform(label_state, Text("State: Panic (Patterned)", color=RED, font_size=36).next_to(title, DOWN)))

        counts_pattern = [2, 4, 2, 4, 2, 4]

        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        ).center()

        self.play(Create(axes), running_time= 1.5)

        points = []
        for i, count in enumerate(counts_pattern):
            new_stack = get_marbles(count, color=RED).move_to(axes.c2p(i+1, count/2))
            dot = Dot(point=axes.c2p(i+1, count), color=YELLOW)
            points.append(dot.get_center())
            self.add(new_stack, dot)
            self.wait(0.3)
            self.remove(new_stack)

        path = VMobject()
        path.set_points_as_corners(points)
        path.set_color(YELLOW)

        prediction_text = Text("PREDICTABLE!", font_size=48, color=RED, weight=BOLD).move_to(ORIGIN)

        self.play(Create(path))
        self.play(FadeIn(prediction_text, scale=1.5))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
