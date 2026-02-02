from manim import *
import numpy as np

class BenfordMasterclass(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        line_length = 10
        start_point = LEFT * 5 + UP * 2.5

        main_line = Line(start_point, start_point + RIGHT * 10, stroke_width=4, color=GREY)

        ticks = VGroup()
        labels = VGroup()
        segments = VGroup()

        for i in range(1, 11):
            log_pos = np.log10(i)
            x_pos = start_point[0] + (log_pos * line_length)
            position = np.array([x_pos, 2.5, 0])

            tick = Line(DOWN * 0.2, UP * 0.2, stroke_width=3, color=WHITE).move_to(position)
            ticks.add(tick)

            label = Text(str(i), font_size=24).next_to(tick, UP, buff=0.2)
            labels.add(label)

            if i < 10:
                next_log_pos = np.log10(i + 1)
                next_x_pos = start_point[0] + (next_log_pos * line_length)
                mid_x = (x_pos + next_x_pos) / 2
                seg_width = next_x_pos - x_pos

                segment = Rectangle(width=seg_width, height=0.3, fill_opacity=0.3, stroke_width=0)
                segment.move_to(np.array([mid_x, 2.5, 0]))

                if i == 1:
                    segment.set_fill(RED)
                    segment.set_opacity(0.8)
                elif i == 9:
                    segment.set_fill(BLUE)
                    segment.set_opacity(0.8)
                else:
                    segment.set_fill(GREY_D)
                    segment.set_opacity(0.2)

                segments.add(segment)

        line_group = VGroup(main_line, ticks, labels, segments)

        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=3.5,
            axis_config={"include_tip": False, "color": GREY},
            tips=False
        ).shift(DOWN * 1.5)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="1/x")

        graph = axes.plot(lambda x: 1/x, x_range=[1, 10], color=BLUE, stroke_width=4)
        graph_label = MathTex(r"f(x) = \frac{1}{x}", color=BLUE).next_to(graph, UP, buff=0.1).shift(RIGHT*2)

        graph_group = VGroup(axes, axes_labels, graph, graph_label)

        self.play(FadeIn(line_group), run_time=2)
        self.wait(2)

        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait(3)

        seg_1 = segments[0]
        brace_line_1 = Brace(seg_1, DOWN, buff=0.1)

        area_1 = axes.get_area(graph, x_range=[1, 2], color=RED, opacity=0.5)
        label_area_1 = MathTex(r"\int_{1}^{2} \frac{1}{x} dx", color=RED, font_size=30).move_to(area_1).shift(UP*0.5 + RIGHT*0.3)

        self.play(
            seg_1.animate.set_color(RED),
            GrowFromCenter(brace_line_1),
            FadeIn(area_1),
            Write(label_area_1)
        )
        self.wait(3)

        deriv_1 = MathTex(r"= [\ln(x)]_{1}^{2}", color=YELLOW, font_size=36)
        deriv_2 = MathTex(r"= \ln(2) - \ln(1)", color=YELLOW, font_size=36)
        deriv_3 = MathTex(r"= \ln(1 + \frac{1}{1})", color=YELLOW, font_size=36)

        deriv_group = VGroup(deriv_1, deriv_2, deriv_3).arrange(DOWN, aligned_edge=LEFT)
        deriv_group.next_to(label_area_1, RIGHT, buff=1).shift(UP * 0.5)

        self.play(Write(deriv_group), run_time=2)
        self.wait(4)

        seg_9 = segments[-1]
        brace_line_9 = Brace(seg_9, DOWN, buff=0.1)

        area_9 = axes.get_area(graph, x_range=[9, 10], color=BLUE, opacity=0.5)

        self.play(
            FadeOut(label_area_1), FadeOut(deriv_group), FadeOut(brace_line_1),
            seg_1.animate.set_opacity(0.3), area_1.animate.set_opacity(0.2),

            seg_9.animate.set_color(BLUE).set_opacity(1),
            GrowFromCenter(brace_line_9),
            FadeIn(area_9)
        )

        label_area_9 = MathTex(r"\int_{9}^{10} \frac{1}{x} dx", color=BLUE, font_size=30).next_to(area_9, UP, buff=0.1)
        self.play(Write(label_area_9))
        self.wait(2)

        deriv_9 = MathTex(r"= \ln(1 + \frac{1}{9})", color=BLUE, font_size=36).next_to(label_area_9, UP, buff=0.2)
        self.play(Write(deriv_9))
        self.wait(4)

        self.play(
            FadeOut(label_area_9), FadeOut(deriv_9), FadeOut(brace_line_9),
            seg_9.animate.set_opacity(0.3), area_9.animate.set_opacity(0.2),
            FadeOut(graph_group), FadeOut(line_group)
        )

        final_text = Text("General Formula", font_size=30, color=GREY).to_edge(UP, buff=2)

        formula_ln = MathTex(r"P(d) = \frac{\int_{d}^{d+1} \frac{1}{x} dx}{\int_{1}^{10} \frac{1}{x} dx}", font_size=50)
        formula_log = MathTex(r"P(d) = \log_{10}(1 + \frac{1}{d})", font_size=70, color=YELLOW)

        self.play(Write(final_text), Write(formula_ln))
        self.wait(3)

        self.play(TransformMatchingTex(formula_ln, formula_log))
        self.play(Circumscribe(formula_log, color=YELLOW))
        self.wait(4)

        self.play(FadeOut(formula_log), FadeOut(final_text))
        self.wait(5)
