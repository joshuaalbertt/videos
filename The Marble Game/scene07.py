from manim import *

# KONSTANTA WARNA
COLOR_MARBLE = GOLD_E
COLOR_GRID = GREY_D
COLOR_BG = BLACK
COLOR_SQUID_PINK = "#ED1B76" # Pink khas Squid Game

class ClosingScene(ThreeDScene):
    def construct(self):
        # --- SETUP VISUAL 3D ---
        # Posisi awal kamera (Agak tinggi dan menyamping)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.6)

        # 1. 3D Grid Floor
        grid = NumberPlane(
            x_range=[-25, 25, 1],
            y_range=[-25, 25, 1],
            background_line_style={
                "stroke_color": COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }
        )
        # Menambahkan Axis Config agar sumbu Y dan X juga terpengaruh warna/style yang konsisten
        grid.axes.set_stroke(color=COLOR_GRID, opacity=0.5)

        # 2. Kelereng 3D (Sphere)
        marble = Sphere(radius=0.4, color=COLOR_MARBLE, resolution=(24, 24))
        marble.set_sheen(0.8, direction=UL) # Efek kilau metalik/kaca
        marble.move_to(ORIGIN + OUT * 0.4) # Naikkan sedikit agar duduk di atas grid

        self.add(grid, marble)

        # Mulai rotasi kamera pelan (Cinematic feel)
        self.begin_ambient_camera_rotation(rate=0.08)

        # --- VO 1: KEPUTUSAN YANG BENAR (~5 detik) ---
        # "Dalam permainan seperti ini, keputusan yang benar tidak selalu menyelamatkan."

        # Zoom in perlahan
        self.move_camera(
            zoom=0.8,
            run_time=5
        )

        # --- VO 2: STRUKTUR & PILIHAN (~5 detik) ---
        # "Terkadang, strukturnya memang tidak memberi pilihan."

        # VISUAL: Grid memudar (Kehampaan)
        # FIX: Memisahkan animasi fade out untuk axes dan background_lines agar mulus
        self.play(
            grid.background_lines.animate.set_stroke(opacity=0),
            grid.axes.animate.set_stroke(opacity=0),
            run_time=4
        )
        self.remove(grid)

        self.wait(1)

        # --- VO 3: SIGNATURE "JOSHUA" (~2 detik) ---
        # "Joshua."

        # 1. Stop rotasi kamera agar orientasi terkendali
        self.stop_ambient_camera_rotation()

        # 2. Pindahkan kamera ke posisi "Low Angle Front" yang dramatis
        # Phi = 80 (Rendah/Dekat tanah), Theta = -90 (Depan lurus)
        self.move_camera(
            phi=80 * DEGREES,
            theta=-90 * DEGREES,
            zoom=1.2,
            run_time=2
        )

        # TRANSISI UNIK: Kelereng (Bulat) berubah menjadi Kotak (Simbol Q.E.D / Squid Game)

        qed_square = Square(side_length=1.5, fill_opacity=1, color=COLOR_SQUID_PINK)
        qed_square.set_stroke(width=0)

        # Text Math: Q.E.D.
        text_qed = Text("Q.E.D.", font="serif", font_size=36, color=WHITE)
        text_qed.next_to(qed_square, UP, buff=0.2)

        text_desc = Text("Proof Complete", font="sans-serif", font_size=18, color=GREY)
        text_desc.next_to(qed_square, DOWN, buff=0.2)

        # Grouping elemen akhir
        final_group = VGroup(qed_square, text_qed, text_desc)
        final_group.move_to(marble.get_center())

        # FIX ROTASI ABSOLUT:
        # Putar 90 derajat di sumbu X agar berdiri tegak menghadap kamera (karena kamera di Theta -90)
        final_group.rotate(90 * DEGREES, axis=RIGHT)

        self.play(
            ReplacementTransform(marble, qed_square),
            run_time=1.5
        )

        self.play(
            Write(text_qed),
            FadeIn(text_desc),
            run_time=2
        )

        self.wait(2)

        # Fade to Black
        self.play(
            FadeOut(final_group),
            run_time=2
        )
        self.wait(1)
