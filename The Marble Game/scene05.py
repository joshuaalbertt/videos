from manim import *
import numpy as np

# KONSTANTA WARNA
COLOR_CURVE = BLUE
COLOR_OPTIMAL = YELLOW
COLOR_CRASH = RED
COLOR_AXIS = GREY
COLOR_TEXT = WHITE

class OptimalStopping(Scene):
    def construct(self):
        # --- VO 1: INTRO (~5 detik) ---
        # "Game ini tidak hanya tentang memilih angka. Ini tentang memilih kapan berhenti bermain."

        # 1. Setup Axes
        axes = Axes(
            x_range=[0, 32, 5],
            y_range=[0, 100, 25],
            x_length=10,
            y_length=5.5,
            axis_config={"color": COLOR_AXIS, "include_numbers": True},
        ).to_edge(DOWN).shift(UP * 0.5)

        # Label Sumbu
        x_label = axes.get_x_axis_label("Time (Minutes)", edge=DOWN, direction=DOWN, buff=0.2)
        y_label_text = Text("Expected Value (Win Prob)", font_size=24, color=COLOR_AXIS).rotate(90 * DEGREES)
        y_label = y_label_text.next_to(axes.get_edge_center(LEFT), LEFT, buff=0.7)

        # Diperlambat sedikit untuk intro
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=3)
        self.wait(2) # Jeda untuk menyelesaikan kalimat intro

        # --- VO 2: DEFINISI MASALAH (~10-12 detik) ---
        # "Dengan waktu 30 menit... mirip optimal stopping problem... versi destruktif."

        def ev_function(x):
            if x <= 6:
                return 40 + (50 * np.sin(x/6 * PI/2))
            else:
                return 90 - 2.5 * ((x - 6)**1.2)

        curve = axes.plot(ev_function, x_range=[0, 30], color=COLOR_CURVE)

        # Diperlambat agar kurva naik seiring penjelasan panjang tentang "Secretary Problem"
        self.play(
            Create(curve, rate_func=linear),
            run_time=8
        )
        self.wait(1)

        # --- VO 3: TITIK OPTIMAL & VOLATILITAS (~10 detik) ---
        # "Pemain yang sudah unggul harus berhenti lebih cepat..."

        optimal_x = 6
        optimal_y = ev_function(optimal_x)
        optimal_point = Dot(axes.c2p(optimal_x, optimal_y), color=COLOR_OPTIMAL, radius=0.15)
        optimal_ring = Circle(radius=0.3, color=COLOR_OPTIMAL).move_to(optimal_point)

        label_optimal = Text("Optimal Stopping Point", font_size=20, color=COLOR_OPTIMAL).next_to(optimal_point, UL, buff=0.2)

        self.play(
            FadeIn(optimal_point),
            Create(optimal_ring),
            Write(label_optimal),
            run_time=1.5
        )

        line_drop = DashedLine(optimal_point.get_center(), axes.c2p(optimal_x, 0), color=COLOR_OPTIMAL)
        self.play(Create(line_drop), run_time=1)
        self.wait(2) # Jeda pas di kalimat "berhenti lebih cepat"

        # "...Setiap ronde tambahan meningkatkan volatilitas yang tidak diperlukan."
        curve_crash = axes.plot(ev_function, x_range=[6, 30], color=COLOR_CRASH)

        # Animasi turun merah (crash) saat VO bicara "volatilitas"
        self.play(Create(curve_crash), run_time=4)

        volatility_text = Text("Unnecessary Volatility", font_size=24, color=COLOR_CRASH)
        volatility_text.move_to(axes.c2p(22, 50))

        arrow_volatility = Arrow(start=volatility_text.get_bottom(), end=axes.c2p(20, ev_function(20)), color=COLOR_CRASH)

        self.play(FadeIn(volatility_text), GrowArrow(arrow_volatility), run_time=1.5)
        self.wait(1)

        # --- VO 4: STRATEGI TERTINGGAL / KESIMPULAN (~8-10 detik) ---
        # "Pemain yang tertinggal justru harus memperpanjang... menambah peluang keberuntungan."

        main_text = Text("Stop early when ahead", font_size=40, color=YELLOW, weight=BOLD) # Typo 4O -> 40 fixed
        main_text.to_edge(UR, buff=1.0)

        box_main = SurroundingRectangle(main_text, color=YELLOW, buff=0.2, fill_color=BLACK, fill_opacity=0.8)

        # Muncul saat VO membahas kontras strategi (tertinggal vs unggul) -> fokus ke inti pesan
        self.play(
            Create(box_main),
            Write(main_text),
            FadeOut(volatility_text), FadeOut(arrow_volatility),
            run_time=2
        )

        # Wait lama di akhir untuk penutup VO
        self.wait(5)

        # --- FADE OUT ALL ---
        # FIX: Menghilangkan semua mobject yang ada di layar
        final_mobjects = [
            axes, x_label, y_label, curve, curve_crash,
            optimal_point, optimal_ring, label_optimal, line_drop,
            box_main, main_text
        ]
        self.play(
            *[FadeOut(mob) for mob in final_mobjects],
            run_time=1.5
        )
