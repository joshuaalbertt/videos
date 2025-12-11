from manim import *

# KONSTANTA WARNA
COLOR_THEME = TEAL
COLOR_ICON = WHITE
COLOR_TEXT = GOLD
COLOR_CONNECT = BLUE_E

class MathSummary(Scene):
    def construct(self):
        # --- VO 1: INTRO (~12 detik) ---
        # "Marble Game bukan permainan tebak angka. Ini adalah eksperimen teori keputusan..."

        # Judul Utama
        title = Text("THE DECISION THEORY EXPERIMENT", font_size=40, color=COLOR_THEME, weight=BOLD)
        subtitle = Text("Structure of Failure", font_size=24, color=GREY).next_to(title, DOWN)

        self.play(Write(title), FadeIn(subtitle), run_time=3)
        self.wait(9) # Jeda panjang untuk narasi filosofis awal

        # Geser judul ke atas untuk memberi ruang ikon
        self.play(
            title.animate.scale(0.8).to_edge(UP),
            FadeOut(subtitle),
            run_time=1.5
        )

        # --- SETUP POSISI IKON (Circular Layout) ---
        # Kita gunakan 4 kuadran: UL, UR, DR, DL
        radius = 2.5
        pos_1 = LEFT * 2 + UP * 1.5    # Asimetri Informasi (UL)
        pos_2 = RIGHT * 2 + UP * 1.5   # Variansi (UR)
        pos_3 = RIGHT * 2 + DOWN * 1.5 # Sinyal Palsu (DR)
        pos_4 = LEFT * 2 + DOWN * 1.5  # Stopping Point (DL)

        # --- ICON 1: ASIMETRI INFORMASI (VO 2: ~4-5s) ---
        # Visual: Dua bar chart tidak seimbang (Information Gap)
        icon_1_group = VGroup()
        bar_a = Rectangle(height=1.5, width=0.4, color=COLOR_ICON)
        bar_b = Rectangle(height=0.5, width=0.4, color=GREY, fill_opacity=0.5).next_to(bar_a, RIGHT, buff=0.2, aligned_edge=DOWN)
        gap_arrow = DoubleArrow(bar_a.get_top(), bar_b.get_top() + UP*1, color=RED, buff=0.1).scale(0.5)

        icon_1_group.add(bar_a, bar_b, gap_arrow).move_to(pos_1)
        label_1 = Text("Information Gap", font_size=20, color=COLOR_TEXT).next_to(icon_1_group, LEFT)

        self.play(
            FadeIn(icon_1_group, shift=DOWN),
            Write(label_1),
            run_time=1.5
        )
        self.wait(2.5)

        # --- ICON 2: VARIANSI (VO 3: ~4-5s) ---
        # Visual: Kurva gelombang sinus (High Volatility)
        icon_2_group = VGroup()
        axes_small = Axes(x_range=[0, 4], y_range=[-1, 1], x_length=2, y_length=1.5, axis_config={"include_tip": False})
        wave = axes_small.plot(lambda x: 0.8 * np.sin(3*x), color=RED)

        icon_2_group.add(axes_small, wave).move_to(pos_2)
        label_2 = Text("High Variance", font_size=20, color=COLOR_TEXT).next_to(icon_2_group, RIGHT)

        self.play(
            Create(wave),
            FadeIn(axes_small),
            Write(label_2),
            run_time=1.5
        )
        self.wait(2.5)

        # --- ICON 3: SINYAL PALSU (VO 4: ~4-5s) ---
        # Visual: Lingkaran sinyal dengan tanda silang (Bluff)
        icon_3_group = VGroup()
        circle_sig = Circle(radius=0.6, color=COLOR_ICON)
        cross = Cross(circle_sig, color=RED).scale(0.6)

        icon_3_group.add(circle_sig, cross).move_to(pos_3)
        label_3 = Text("False Signal", font_size=20, color=COLOR_TEXT).next_to(icon_3_group, RIGHT)

        self.play(
            Create(circle_sig),
            Create(cross),
            Write(label_3),
            run_time=1.5
        )
        self.wait(2.5)

        # --- ICON 4: STOPPING POINT (VO 5: ~5s) ---
        # Visual: Kurva naik lalu titik stop (Optimal Stop)
        icon_4_group = VGroup()
        arc_path = Arc(radius=0.8, start_angle=180*DEGREES, angle=180*DEGREES, color=BLUE)
        stop_dot = Dot(color=YELLOW).move_to(arc_path.get_top())

        icon_4_group.add(arc_path, stop_dot).move_to(pos_4)
        label_4 = Text("Stopping Point", font_size=20, color=COLOR_TEXT).next_to(icon_4_group, LEFT)

        self.play(
            Create(arc_path),
            FadeIn(stop_dot),
            Write(label_4),
            run_time=1.5
        )
        self.wait(3.5)

        # --- FINAL: CONNECTING THE DOTS (VO: Closing) ---
        # Menghubungkan semua ikon menjadi lingkaran/siklus yang rapi

        # Buat lingkaran besar yang menghubungkan pusat-pusat ikon
        connecting_circle = Circle(radius=2.83, color=COLOR_CONNECT, stroke_width=2).move_to(ORIGIN) # radius approx sqrt(2^2 + 2^2)

        # Garis penghubung antar node (diamond shape)
        lines = VGroup(
            Line(pos_1, pos_2, color=COLOR_CONNECT),
            Line(pos_2, pos_3, color=COLOR_CONNECT),
            Line(pos_3, pos_4, color=COLOR_CONNECT),
            Line(pos_4, pos_1, color=COLOR_CONNECT)
        )

        center_text = Text("Game Structure", font_size=24, color=WHITE).move_to(ORIGIN)

        self.play(
            Create(lines),
            FadeIn(center_text),
            # Putar ikon sedikit agar terlihat dinamis
            Rotate(icon_1_group, angle=360*DEGREES, rate_func=smooth, about_point=pos_1),
            Rotate(icon_2_group, angle=360*DEGREES, rate_func=smooth, about_point=pos_2),
            Rotate(icon_3_group, angle=360*DEGREES, rate_func=smooth, about_point=pos_3),
            Rotate(icon_4_group, angle=360*DEGREES, rate_func=smooth, about_point=pos_4),
            run_time=3
        )

        self.wait(3)

        # Fade Out All
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
