from manim import *

class Scene01(Scene):
    def construct(self):
        # ==========================================
        # 1. DEFINISI OBJEK (SETUP)
        # ==========================================

        # --- Text Kecil: Rules (Diubah menjadi Rules: Bebas agar sesuai VO) ---
        rules_text = Text("CONTEXT", font_size=32, color=GRAY_B)
        rules_text.to_edge(UP * 1.0) # Menggunakan UP * 1.0 agar tidak terlalu mepet ke atas

        # --- Player A Setup ---
        box_a = Square(side_length=2.5, color=BLUE_D, fill_color=BLUE_A, fill_opacity=0.5)
        box_a.shift(LEFT * 3.5)

        label_a = Text("Player A", font_size=28, weight=BOLD).next_to(box_a, UP)
        var_a_text = Text("A = ", font_size=36)
        var_a_int = Integer(10, font_size=36, color=YELLOW)
        var_a = VGroup(var_a_text, var_a_int).arrange(RIGHT, buff=0.1).move_to(box_a.get_center())

        player_a_group = VGroup(box_a, label_a, var_a)


        # --- Player B Setup ---
        box_b = Square(side_length=2.5, color=RED_D, fill_color=RED_A, fill_opacity=0.5)
        box_b.shift(RIGHT * 3.5)

        label_b = Text("Player B", font_size=28, weight=BOLD).next_to(box_b, UP)
        var_b_text = Text("B = ", font_size=36)
        var_b_int = Integer(10, font_size=36, color=YELLOW)
        var_b = VGroup(var_b_text, var_b_int).arrange(RIGHT, buff=0.1).move_to(box_b.get_center())

        player_b_group = VGroup(box_b, label_b, var_b)


        # --- Objek Koneksi (Information Gap) ---
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

        # Grup semua objek untuk Fade Out
        all_objects = VGroup(
            rules_text,
            player_a_group,
            player_b_group,
            connection_line,
            gap_text,
            q_mark
        )


        # ==========================================
        # 2. URUTAN ANIMASI (Disesuaikan dengan VO)
        # ==========================================

        # VO: “Setiap pasangan diberi sepuluh kelereng. Tujuannya jelas: kumpulkan dua puluh.” (± 4.0 detik)
        self.play(Write(rules_text), run_time=1.3) # Munculkan "Rules" (Context)
        self.play(
            DrawBorderThenFill(box_a),
            Write(label_a),
            DrawBorderThenFill(box_b),
            Write(label_b),
            run_time=2.0 # Kotak dan label muncul
        )
        self.play(
            Write(var_a),
            Write(var_b),
            run_time=1.5 # Nilai 10 muncul
        )

        # VO: “Tidak ada batasan permainan. Mereka boleh menggunakan game apapun yang disepakati berdua.” (± 4.5 detik)
        self.wait(4.5) # Jeda untuk narasi rules/gameplay

        # VO: “Sekilas, ini terlihat seperti permainan keputusan biasa.” (± 2.5 detik)
        # Mulai animasi garis koneksi saat narasi membahas "permainan biasa"
        self.play(GrowFromCenter(connection_line), run_time=2.0)
        self.wait(0.5) # Jeda singkat sebelum pergeseran narasi

        # VO: “Tapi kalau kita melihat strukturnya, game ini penuh asimetri informasi, manipulasi probabilitas, dan strategi optimal yang tidak pernah disebutkan di layar.” (± 8.0 detik)

        # 1. Teks "Information Gap" muncul bersamaan dengan kata "asimetri informasi"
        self.play(Write(gap_text), run_time=1.5)

        # 2. Tanda tanya (ketidakpastian) muncul sebagai penekanan
        self.play(FadeIn(q_mark, shift=UP*0.2), run_time=1.0)

        # 3. Tahan tampilan akhir untuk sisa narasi (strategi optimal)
        self.wait(6.0)

        # ==========================================
        # 3. FADE OUT (Penghapusan Semua Objek)
        # ==========================================

        # Animasi FadeOut
        self.play(
            FadeOut(all_objects, run_time=1.5)
        )

        self.wait(0.5)
