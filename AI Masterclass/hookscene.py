from manim import *
import numpy as np
import random

class AIHook(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        text_1 = Text("The illusion of AI.", font_size=48, weight=BOLD)
        self.play(Write(text_1))
        self.wait(1)
        self.play(FadeOut(text_1, shift=UP))

        nodes = VGroup(*[Dot(radius=0.06, color=BLUE) for _ in range(60)])
        for node in nodes:
            node.move_to([random.uniform(-6, 6), random.uniform(-3, 3), 0])

        edges = VGroup()
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                dist = np.linalg.norm(nodes[i].get_center() - nodes[j].get_center())
                if dist < 1.8:
                    edge_color = interpolate_color(BLUE_E, GREY_D, dist/1.8)
                    edges.add(Line(nodes[i].get_center(), nodes[j].get_center(), stroke_width=0.8, color=edge_color, stroke_opacity=0.6))

        network = VGroup(edges, nodes)

        self.play(Create(network, run_time=2.5, lag_ratio=0.05))

        text_2 = Text("A digital brain?", font_size=36, color=GREY_A).to_edge(DOWN, buff=1)
        self.play(FadeIn(text_2, shift=UP))

        self.play(
            network.animate.scale(1.1).rotate(5 * DEGREES),
            run_time=3,
            rate_func=there_and_back
        )

        eq = MathTex(r"f(x) = \max(0, Wx + b)", font_size=80, color=WHITE)

        self.play(
            FadeOut(text_2),
            ReplacementTransform(network, eq),
            run_time=1.5
        )
        self.wait(1)

        text_3 = Text("No. Just functions.", font_size=36, color=YELLOW).next_to(eq, DOWN, buff=1)
        self.play(Write(text_3))
        self.wait(2)

        self.play(FadeOut(eq), FadeOut(text_3))

        title = Text("AI MASTERCLASS", font_size=60, weight=BOLD).set_letter_spacing(0.1)
        subtitle = Text("The Mathematics of Intelligence", font_size=30, color=GREY).next_to(title, DOWN, buff=0.3)

        title_group = VGroup(title, subtitle).move_to(ORIGIN)

        self.play(FadeIn(title_group, shift=DOWN*0.5))
        self.wait(3)

        self.play(FadeOut(title_group))
