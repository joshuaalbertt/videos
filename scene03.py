from manim import *
import numpy as np

# KONSTANTA WARNA
COLOR_SAFE = BLUE_C      # Player A (Low Variance)
COLOR_RISKY = RED_C      # Player B (High Variance)
COLOR_AXIS = GREY
COLOR_TEXT = WHITE

class ProbabilityExploitation(Scene):
    def construct(self):
        # --- SCENE 1: VISUALISASI VARIANSI (10 Ronde) ---

        # === VO BAGIAN 1 (Intro & Strategi) ~ 10-12 detik ===
        # "Permainan ini terlihat seperti ‘tebak angka acak’..."

        # 1. Setup Grafik
        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 25, 5],
            x_length=10,
            y_length=6,
            axis_config={"color": COLOR_AXIS, "include_numbers": True},
            tips=False
        ).to_edge(DOWN).shift(UP * 0.5)

        x_label = axes.get_x_axis_label("Rounds", edge=DOWN, direction=DOWN, buff=0.2)

        # Text Marbles Vertikal (Sesuai request sebelumnya)
        marbles_text = Text("Marbles", color=COLOR_AXIS, font_size=36).rotate(90 * DEGREES)
        y_label = marbles_text.next_to(axes.get_edge_center(LEFT), LEFT, buff=0.7)

        target_line = DashedLine(start=axes.c2p(0, 20), end=axes.c2p(11, 20), color=GREEN)
        zero_line = DashedLine(start=axes.c2p(0, 0), end=axes.c2p(11, 0), color=GREY)

        # Animasi Setup (4 detik) - Pas kalimat pertama
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )
        self.play(Create(target_line), Create(zero_line), run_time=1)

        # "...Tetapi sebenarnya, pemain memiliki dua strategi probabilitas..."
        # Teks A dan B muncul
        text_A = Text("Player A: Low Variance", font_size=24, color=COLOR_SAFE)
        text_B = Text("Player B: High Variance", font_size=24, color=COLOR_RISKY)
        legend_group = VGroup(text_A, text_B).arrange(RIGHT, buff=2).to_edge(UP)

        # Munculkan Legend (2 detik) + Wait (2 detik) untuk menyelesaikan kalimat VO 1
        self.play(Write(legend_group), run_time=2)
        self.wait(2)


        # === VO BAGIAN 2 (Player A) ~ 12-14 detik ===
        # "Jika Player A unggul jauh, strategi optimalnya adalah bermain konservatif..."

        y_values_A = [15, 16, 15, 16, 17, 16, 15, 16, 17, 18, 17]
        graph_A = axes.plot_line_graph(
            x_values=list(range(11)), y_values=y_values_A, line_color=COLOR_SAFE,
            add_vertex_dots=True, vertex_dot_radius=0.06
        )

        # Animasi Grafik A (8 detik) - Lambat agar sesuai penjelasan panjang
        self.play(Create(graph_A), run_time=8, rate_func=linear)

        # "...semakin kecil peluang kekalahan jika ia menjaga perubahan kelereng tetap kecil."
        # Highlight A
        rect_A = SurroundingRectangle(graph_A, color=COLOR_SAFE, buff=0.1, stroke_opacity=0.5)
        self.play(Create(rect_A), run_time=1)
        self.play(FadeOut(rect_A), run_time=1)
        self.wait(1) # Jeda sebelum masuk ke Player B


        # === VO BAGIAN 3 (Player B) ~ 12-14 detik ===
        # "Sebaliknya, Player B yang hampir kalah berada dalam posisi ditekan oleh probabilitas..."

        y_values_B = [5, 10, 5, 12, 4, 8, 16, 8, 16, 22, 20]
        graph_B = axes.plot_line_graph(
            x_values=list(range(11)), y_values=y_values_B, line_color=COLOR_RISKY,
            add_vertex_dots=True, vertex_dot_radius=0.06
        )

        # Animasi Grafik B (8 detik) - Bergerak naik turun saat VO bicara risiko
        self.play(Create(graph_B), run_time=8, rate_func=linear)

        # "...semakin besar peluang membalikkan keadaan."
        # Highlight B
        rect_B = SurroundingRectangle(graph_B, color=COLOR_RISKY, buff=0.1, stroke_opacity=0.5)
        self.play(Create(rect_B), run_time=1)
        self.play(FadeOut(rect_B), run_time=1)

        # Transisi Keluar
        self.wait(1)
        self.play(
            FadeOut(axes), FadeOut(graph_A), FadeOut(graph_B),
            FadeOut(legend_group), FadeOut(x_label), FadeOut(y_label),
            FadeOut(target_line), FadeOut(zero_line),
            run_time=1.5
        )

        # --- SCENE 2: DIAGRAM TEORI (Masuk ke VO 4 dst) ---

        axes_theory = Axes(
            x_range=[0, 10, 1], y_range=[0, 1, 0.25],
            x_length=8, y_length=5,
            axis_config={"include_tip": True, "color": WHITE}, tips=True
        ).center().shift(DOWN * 0.5)

        label_x_theory = axes_theory.get_x_axis_label("Variance (Risk)", edge=DOWN, direction=DOWN)
        y_theory_text = Text("Win Probability", color=WHITE, font_size=36).rotate(90 * DEGREES)
        label_y_theory = y_theory_text.next_to(axes_theory.get_edge_center(LEFT), LEFT, buff=0.5)

        self.play(Create(axes_theory), Write(label_x_theory), Write(label_y_theory))

        curve_losing = axes_theory.plot(lambda x: 0.1 + 0.4 * np.log(x + 1)/np.log(11), x_range=[0, 10], color=COLOR_RISKY)
        curve_winning = axes_theory.plot(lambda x: 0.9 - 0.4 * (x/10)**2, x_range=[0, 10], color=COLOR_SAFE)

        self.play(Create(curve_losing), run_time=2)
        self.play(Create(curve_winning), run_time=2)

        label_losing = Text("Player B (Behind)", font_size=20, color=COLOR_RISKY).next_to(curve_losing.get_end(), RIGHT + UP, buff=0.2)
        label_winning = Text("Player A (Ahead)", font_size=20, color=COLOR_SAFE).next_to(curve_winning.get_end(), RIGHT + DOWN, buff=0.2)

        self.play(FadeIn(label_losing), FadeIn(label_winning))

        conclusion_text = Text("High Variance = Comeback Chance", font_size=36, color=YELLOW)
        conclusion_text.to_edge(UP, buff=1)

        dot_focus = Dot(axes_theory.c2p(9, curve_losing.underlying_function(9)), color=YELLOW)
        circle_focus = Circle(radius=0.5, color=YELLOW).move_to(dot_focus)

        self.play(Write(conclusion_text))
        self.play(FocusOn(dot_focus), Create(circle_focus), Indicate(label_losing))

        self.wait(3)
