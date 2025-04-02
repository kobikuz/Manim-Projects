from manim import *

class Gen_mat(Scene):
    def construct(self):
        vec_A = MathTex(r"\begin{pmatrix} A_0 \\ A_1 \\ A_2 \\ A_3 \\ A_4 \\ \vdots \end{pmatrix}"
                        ).to_edge(LEFT)
        color1 = [9,11,13,15,17]
        for color in color1:
            vec_A[0][color].set_color(ORANGE)
        vec_B = MathTex(r"\begin{pmatrix} B_0 \\ B_1 \\ B_2 \\ B_3 \\ B_4 \\ \vdots \end{pmatrix}"
                        )
        color2 = [9,11,13,15,17]
        for color in color2:
            vec_B[0][color].set_color(BLUE)
        vec_C = MathTex(r"\begin{pmatrix} C_0 \\ C_1 \\ C_2 \\ C_3 \\ C_4 \\ \vdots \end{pmatrix}",
                        ).to_edge(RIGHT)
        color3 = [9,11,13,15,17,19]
        for color in color3:
            vec_C[0][color].set_color(PINK)

        Gen_mat = MathTex(r"\begin{pmatrix}"
                  r" A_0 & B_0 & C_0 & \ldots \\"
                  r" A_1 & B_1 & C_1 & \ldots \\"
                  r" A_2 & B_2 & C_2 & \ldots \\"
                  r" A_3 & B_3 & C_3 & \ldots \\"
                  r" A_4 & B_4 & C_4 & \ldots \\"
                  r" \vdots &\vdots & \vdots & \vdots"
                  r"\end{pmatrix}")
        colors11=[9,18,27,36,45]
        colors12=[11,20,29,38,47]
        colors13=[13,22,31,40,49]
        for i in range(len(colors11)):
            Gen_mat[0][colors11[i]].set_color(ORANGE)
            Gen_mat[0][colors12[i]].set_color(BLUE)
            Gen_mat[0][colors13[i]].set_color(PINK)
        br2 = Brace(Gen_mat, LEFT)
        b2_tex = MathTex("r").next_to(br2, LEFT).set_color(YELLOW)
        br3 = Brace(Gen_mat, DOWN)
        b3_tex = MathTex("k").set_color(YELLOW).next_to(br3, DOWN)
        
        self.play(Write(vec_A))
        self.play(Write(vec_B))
        self.play(Write(vec_C))
        self.wait(3)
        self.play(Indicate(vec_A))
        self.wait()
        self.play(Indicate(vec_B))
        self.wait()
        self.play(Indicate(vec_C))
        self.wait()
        self.play(vec_A.animate.next_to(vec_B,LEFT),vec_C.animate.next_to(vec_B,RIGHT),run_time=2,rate_func=smooth)
        br1 = Brace(vec_A, LEFT)
        b1_tex = MathTex("r").next_to(br1, LEFT).set_color(YELLOW)
        self.play(Write(br1), Write(b1_tex))
        self.wait(3)
        self.play(
            Transform(VGroup(vec_A, vec_B, vec_C), Gen_mat),
            Transform(br1, br2),
            Transform(b1_tex, b2_tex)
        )
        self.wait(2)
        self.play(Indicate(b2_tex,scale_factor=1.5))
        self.play(Write(br3), Write(b3_tex))
        self.wait(2)
        self.play(Indicate(b3_tex,scale_factor=1.5))
        self.wait(2)

        self.play(FadeOut( br3, br1,  b1_tex, b3_tex, b2_tex),VGroup(vec_A, vec_B, vec_C).animate.shift(LEFT*2))
        vec_data = MathTex(r"\begin{pmatrix} d_0\\ d_1 \\ d_2 \\ d_3 \\ d_4 \\ \vdots \end{pmatrix}").next_to(Gen_mat,RIGHT).shift(LEFT*2)
        for color in color3:
            vec_data[0][color].set_color(GREEN)
        self.play(Write(vec_data))
        self.wait(2)
        eq = MathTex(r"=").next_to(vec_data,RIGHT)
        vec_t = MathTex(r"\begin{pmatrix} t_0 \\ t_1 \\ t_2 \\ t_3 \\ t_4 \\ \vdots \end{pmatrix}").next_to(eq,RIGHT)
        for color in color3:
            vec_t[0][color].set_color(MAROON)
        self.play(Write(eq))
        self.play(TransformFromCopy(VGroup(vec_data,Gen_mat),vec_t))

        self.wait(2)

