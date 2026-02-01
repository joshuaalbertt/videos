from manim import *

class Scene01(Scene):
    def construct(self):
        rules_text = Text("CONTEXT", font_size=32, color=GRAY_B)
        rules_text.to_edge(UP * 1.0)

        box_a = Square(side_length=2.5, color=BLUE_D, fill_color=BLUE_A, fill_opacity=0.5)
        box_a.shift(LEFT * 3.5)

        label_a = Text("Player A", font_size=28, weight=BOLD).next_to(box_a, UP)
        var_a_text = Text("A = ", font_size=36)
        var_a_int = Integer(10, font_size=36, color=YELLOW)
        var_a = VGroup(var_a_text, var_a_int).arrange(RIGHT, buff=0.1).move_to(box_a.get_center())

        player_a_group = VGroup(box_a, label_a, var_a)

        box_b = Square(side_length=2.5, color=RED_D, fill_color=RED_A, fill_opacity=0.5)
        box_b.shift(RIGHT * 3.5)

        label_b = Text("Player B", font_size=28, weight=BOLD).next_to(box_b, UP)
        var_b_text = Text("B = ", font_size=36)
        var_b_int = Integer(10, font_size=36, color=YELLOW)
        var_b = VGroup(var_b_text, var_b_int).arrange(RIGHT, buff=0.1).move_to(box_b.get_center())

        player_b_group = VGroup(box_b, label_b, var_b)

        connection_line = DoubleArrow(
            start=box_a.get_right(),
            end=box_b.get_left(),
            buff=0.2,
            color=ORANGE,
            stroke_width=6
        )

        gap_text = Text("Information Gap", font_size=32, color=ORANGE)
        gap_text.next_to(connection_line, UP, buff=0.2)

        q_mark = Text("?", font_size=40, color=ORANGE).next_to(connection_line, DOWN)

        all_objects = VGroup(
            rules_text,
            player_a_group,
            player_b_group,
            connection_line,
            gap_text,
            q_mark
        )

        self.play(Write(rules_text), run_time=1.3)
        self.play(
            DrawBorderThenFill(box_a),
            Write(label_a),
            DrawBorderThenFill(box_b),
            Write(label_b),
            run_time=2.0
        )
        self.play(
            Write(var_a),
            Write(var_b),
            run_time=1.5
        )

        self.wait(4.5)

        self.play(GrowFromCenter(connection_line), run_time=2.0)
        self.wait(0.5)
        self.play(Write(gap_text), run_time=1.5)
        self.play(FadeIn(q_mark, shift=UP*0.2), run_time=1.0)
        self.wait(6.0)
        self.play(
            FadeOut(all_objects, run_time=1.5)
        )

        self.wait(0.5)
