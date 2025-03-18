from manim import *

class Matrix_Gen1(Scene):
    def construct(self):
        tx1 = Tex("an ECC is denoted by (m,r,d,q)").shift(UP*2)
        tx21 = MathTex(
            r"\cdot m= \text{word length} "
        ).scale(0.75).next_to(tx1, DOWN, buff=0.5).align_to(tx1,LEFT)
        tx22=MathTex(
            r"\cdot r =  \text{rate (amount of real information transmitted)} "
        ).scale(0.75).next_to(tx21, DOWN, buff=0.5).align_to(tx21,LEFT)
        tx23=MathTex(
            r"\cdot d = \text{distance (minimum distance between codewords)} "
        ).scale(0.75).next_to(tx22, DOWN, buff=0.5).align_to(tx22,LEFT)
        tx24=MathTex(
            r"\cdot q = \text{alphabet size}"
        ).scale(0.75).next_to(tx23, DOWN, buff=0.5).align_to(tx23,LEFT)
        tx3 = Tex("Lets take for example Hamming code(7,4,3,2):").next_to(tx24,DOWN,buff=0.5).align_to(tx1,LEFT)

        self.play(Write(tx1))
        self.wait(0.5)
        self.play(Write(tx21))
        self.wait(0.5)
        self.play(Write(tx22))
        self.wait(0.5)
        self.play(Write(tx23))
        self.wait(0.5)
        self.play(Write(tx24))
        self.wait(0.5)
        self.play(Write(tx3))
        self.wait(1)

        self.play(FadeOut(tx1),FadeOut(tx21),FadeOut(tx22),FadeOut(tx23),FadeOut(tx24),tx3.animate.to_edge(UP))
        self.wait(1)

class Matrix_Gen2(Scene):
    def construct(self):
        tx3 = Tex("Lets take for example Hamming code(7,4,3,2):").to_edge(UP)
        tx4= Tex("The generation matrix of this code is given as:"
                 ).scale(0.75).next_to(tx3, DOWN, buff=0.5).align_to(tx3,LEFT)
        Gen_mat = Matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
                         ).scale(0.75).next_to(tx4, DOWN, buff=0.5).align_to(tx4,LEFT)
        tx51 = Tex("This matrix will transform actual data into codewords,"
                   ).scale(0.5).next_to(Gen_mat, RIGHT, buff=0.25).align_to(Gen_mat, UP)
        tx52= Tex("So when we transmit them, we will be able to recognize and fix errors!"
                  ).scale(0.5).next_to(tx51, DOWN, buff=0.25).align_to(tx51,LEFT)         
        self.play(Write(tx3))
        self.wait(0.5)
        self.play(Write(tx4))
        self.wait(0.5)
        self.play(Write(Gen_mat))
        self.wait(0.5)
        self.play(Write(tx51))
        self.play(Write(tx52))
        self.wait(1)

        ##DUAL CODE##
        tex6= Tex("For every linear ECC we can denote a Dual code as :"
                  ).scale(0.75).next_to(tx3, DOWN, buff=0.25).to_edge(LEFT)
        tex7=MathTex(r"C^{\vee} = \{ w \in Q^m \mid \forall c \in C: \langle w, c \rangle = 0 \}"
                     ).scale(0.75).next_to(tex6, DOWN, buff=0.15).to_edge(LEFT)
        tex8 = MathTex(r"\text{The Generation matrix of } C^{\vee} \text{is ofter reffered as a parity check matrix of C}"
                       ).scale(0.75).next_to(tex7, DOWN, buff=0.15).to_edge(LEFT)
        tex9 = Tex("Lets see why this applies for our code:"
                   ).scale(0.75).next_to(tex8, DOWN, buff=0.15).to_edge(LEFT)
        
        self.play(FadeOut(Gen_mat),FadeOut(tx4),FadeOut(tx51),FadeOut(tx52))
        
        self.play(Write(tex6))
        self.play(Write(tex7)) 
        self.play(Write(tex8))
        self.play(Write(tex9))
        self.wait(1)


class Matrix_Gen3(Scene):
    def construct(self):
        tex9 = Tex("Lets see why this applies for our code:"
            ).scale(0.75).to_corner(UP + LEFT)
        tex7=MathTex(r"C^{\vee} = \{ w \in Q^m \mid \forall c \in C: \langle w, c \rangle = 0 \}"
             ).scale(0.75).next_to(tex9, DOWN, buff=0.15).to_edge(LEFT)
        
        self.play(Write(tex9))
        self.play(Write(tex7))

        tex10 =  Tex("The Hamming(7,4,3) Code is defined as follows:"
                     ).scale(0.75).next_to(tex7, DOWN, buff=0.15).to_edge(LEFT)
        tex11 = MathTex(r"\text{for any codeword x : }x = (x_1, \dots, x_7) \text{ we have :}"
                        ).scale(0.75).next_to(tex10, DOWN, buff=0.15).to_edge(LEFT)
        equations1 = MathTex(r"""
                                \left\{
                                \begin{array}{l}
                                x_1 = x_3 + x_5 + x_7 \mod 2 \\
                                x_2 = x_3 + x_6 + x_7 \mod 2 \\
                                x_4 = x_5 + x_6 + x_7 \mod 2
                                \end{array}
                                \right.
                                """).scale(0.75).next_to(tex11, DOWN, buff=0.15).to_edge(LEFT)

        self.play(Write(tex10))
        self.play(Write(tex11))
        self.play(Write(equations1))
        self.wait(1)

        equal = Tex("=").scale(0.75).next_to(equations1,RIGHT, buff=0.25).align_to(equations1, UP + DOWN)
        equations2 = MathTex(r"""
                                \left\{
                                \begin{array}{l}
                                x_1+x_1 = x_3 + x_5 + x_7+x_1 \mod 2 \\
                                x_2+x_2 = x_3 + x_6 + x_7+x_2 \mod 2 \\
                                x_4+x_4 = x_5 + x_6 + x_7+x_4 \mod 2
                                \end{array}
                                \right.
                                """).scale(0.75).next_to(equal, RIGHT, buff=0.25).align_to(equations1, UP + DOWN)
        self.play(Write(equal))
        self.play(Write(equations2))
        self.wait(1)

        tex12 = MathTex(r"\text{mod } 2 \text{ works as an XOR operator as } |q| = 2 \text{ and } q = \{0,1\} \text{ in binary space}"
                        ).scale(0.65).next_to(equations1, DOWN,buff= 0.5).to_edge(LEFT)
        right_arr1 = MathTex(r"\Rightarrow"
                        ).scale(0.75).next_to(equations2,RIGHT, buff=0.25).align_to(equations2, UP + DOWN)
        
        self.play(Write(tex12))
        self.wait(0.5)
        self.play(Write(right_arr1))
        equations3 = MathTex(r"""
                        \left\{
                        \begin{array}{l}
                        0 = x_3 + x_5 + x_7+x_1 \mod 2 \\
                        0 = x_3 + x_6 + x_7+x_2 \mod 2 \\
                        0 = x_5 + x_6 + x_7+x_4 \mod 2
                        \end{array}
                        \right.
                        """).scale(0.75).next_to(tex12, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(equations3))
        self.wait(0.5)
        equal2 = Tex("=").scale(0.7).next_to(equations3,RIGHT, buff=0.25).align_to(equations3, UP + DOWN)
        equations4 = MathTex(r"""
                            \left\{
                            \begin{array}{l}
                            x_1 + x_3 + x_5 + x_7 = (1,0,1,0,1,0,1) \cdot x = 0 \\
                            x_2 + x_3 + x_6 + x_7 = (0,1,1,0,0,1,1) \cdot x = 0 \\
                            x_4 + x_5 + x_6 + x_7 = (0,0,0,1,1,1,1) \cdot x = 0
                            \end{array}
                            \right.
                            """).scale(0.7).next_to(equal2, RIGHT, buff=0.25).align_to(equations1, UP + DOWN)
        self.play(Write(equal2))
        self.play(Write(equations4))
        self.wait(0.5)

        tex13 = Tex(
                "We identified three vectors that, when multiplied by any \( x \), result in zero,\\ "
                "forming the null space and defining the dual matrix."
            ).scale(0.6).next_to(equations4, DOWN, buff=0.15).to_edge(LEFT)
        self.play(Write(tex13))
        self.wait(1.5)


from manim import *

class Matrix_Gen4(Scene):
    def construct(self):
        ## Showing how the parity check works ##
        tex41 = Tex("Now let's see why the dual matrix is referred to as a parity check matrix"
                    ).set_font_size(36).to_corner(UP + LEFT)
        tex42 = MathTex(r"\text{Let's take a random codeword } x, \text{ say } x = \begin{pmatrix} 0 & 1 & 1 & 0 & 0 & 1 & 1 \end{pmatrix}"
                        ).set_font_size(36).next_to(tex41, DOWN, buff=0.25).to_edge(LEFT)

        shift_up = UP * 0.5  # Shifting everything up slightly

        ## Define the parity check matrix as a MathTex object ##
        parity_check_matrix = MathTex(r"""
            \begin{pmatrix}
            1 & 0 & 1 & 0 & 1 & 0 & 1 \\
            0 & 1 & 1 & 0 & 0 & 1 & 1 \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
            \end{pmatrix}
        """).scale(0.5).next_to(tex42, DOWN, buff=0.5).to_edge(LEFT)

        ## Define vector x as a MathTex object ##
        vector_x = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\ 1 \\ 1
            \end{pmatrix}
        """).scale(0.5).next_to(parity_check_matrix, RIGHT, buff=0.1)

        ## First multiplication: Right arrow + result is zero vector ##
        equal = Tex("=").scale(1).next_to(vector_x, RIGHT, buff=0.1)
        vector_zero = MathTex(r"""
            \begin{pmatrix}
            0 \\ 0 \\ 0
            \end{pmatrix}
        """).scale(0.5).next_to(equal, RIGHT, buff=0.1)

        no_noise = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\ 1 \\ 1
            \end{pmatrix}
        """).scale(0.5).next_to(vector_x, DOWN, buff=0.25).to_edge(LEFT)

        ## Second step: Adding noise vector (0,0,0,0,1,0,0) ##
        plus_sign = MathTex("+").scale(1.2).next_to(no_noise, RIGHT, buff=0.1)
        noise_vector = MathTex(r"""
            \begin{pmatrix}
            0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0
            \end{pmatrix}
        """).scale(0.5).next_to(plus_sign, RIGHT, buff=0.2)
        
        equal1 = Tex("=").scale(1).next_to(noise_vector, RIGHT, buff=0.1)
        new_vector_x = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 1 \\ 1 \\ 1
            \end{pmatrix}
        """).scale(0.5).next_to(equal1, RIGHT, buff=0.2)

        ## Animations ##
        self.play(Write(tex41))
        self.play(Write(tex42))
        self.wait(0.5)

        ## First multiplication ##
        self.play(Write(parity_check_matrix))
        self.play(Write(vector_x))
        self.play(Write(equal))
        self.play(Write(vector_zero))
        self.wait(1)
        noise_vector[0][14].set_color(RED)
        ## Adding noise and creating new vector_x ##
        self.play(Write(no_noise))
        self.play(Write(plus_sign), Write(noise_vector))
        self.play(Write(equal1), Write(new_vector_x),vector_x[0][14].animate.set_color(GREEN),new_vector_x[0][14].animate.set_color(RED))
        self.wait(1)

        #CHECK INDEXES
        #self.add(index_labels(vector_x[0]))
        #self.add(index_labels(new_vector_x[0]))
        
        #new_vector_x[0][14].set_color(RED)
        ## Define second parity check matrix (scaled down) ##
        parity_check_matrix1 = MathTex(r"""
            \begin{pmatrix}
            1 & 0 & 1 & 0 & 1 & 0 & 1 \\
            0 & 1 & 1 & 0 & 0 & 1 & 1 \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
            \end{pmatrix}
        """).scale(0.425).next_to(vector_x, DOWN, buff=0.5).to_edge(LEFT)
        ## Fade out old elements and adjust new layout ##
        self.play(FadeOut(no_noise), FadeOut(plus_sign), FadeOut(equal1), FadeOut(noise_vector),
                  parity_check_matrix.animate.scale(0.85).next_to(tex42, DOWN, buff=0.5).to_edge(LEFT))
        self.play(new_vector_x.animate.next_to(vector_x, DOWN))
        self.play(Write(parity_check_matrix1))
        self.wait(1)
        equal2 = Tex("=").scale(1).next_to(new_vector_x, RIGHT, buff=0.1)
        syndrome1 = MathTex(r"""
            \begin{pmatrix}
            1 \\ 0 \\ 1
            \end{pmatrix}
        """).scale(0.5).next_to(equal2, RIGHT, buff=0.1)
        self.play(Write(equal2),Write(syndrome1),syndrome1[0][2].animate.set_color(RED),syndrome1[0][4].animate.set_color(RED))
       ## self.add(index_labels(syndrome1[0]))
        self.wait(2)
        tex43 = Tex("This vector's name is Syndore vector, and its pointing to the location of the corrupted bit!"
        ).set_font_size(36).next_to(new_vector_x, DOWN, buff=0.25).to_edge(LEFT)
        tex44 = MathTex(r"\text{Why? Because the parity bits were chosen to be on } 2^i \text{ indexes}"
        ).set_font_size(36).next_to(tex43, DOWN, buff=0.25)
        self.play(Write(tex43))
        self.play(Write(tex44))
        self.wait(2)

class Hamming_Code_example(Scene):
    def construct(self):  
        ##show grid
        #grid = NumberPlane()
        #self.add(grid)
        ##
        tex50 = Tex("Now lets see a full example of Sending and error correcting:").to_edge(UP)
        parity_check_matrix = MathTex(r"""
            \begin{bmatrix}
            1 & 1 & 0 & 1 \\
            1 & 0 & 1 & 1 \\
            1 & 0 & 0 & 0 \\
            0 & 1 & 1 & 1 \\
            0 & 1 & 0 & 0 \\
            0 & 0 & 1 & 0 \\
            0 & 0 & 0 & 1
            \end{bmatrix}
        """).scale(0.4).to_edge(LEFT)
        self.play(Write(tex50))
        self.wait(1)
        data_vactor1 = MathTex(r"""
            \begin{pmatrix}
            1 \\ 0 \\ 1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(parity_check_matrix, RIGHT, buff=0.1)
        data_tex = MathTex(r"\vec{d}").next_to(data_vactor1,UP).shift(UP/2)      
        parity_check_matrix_tex = MathTex("\mathbf{G}").next_to(parity_check_matrix,UP).align_to(data_tex,DOWN)
        equal1 = Tex("=").next_to(data_vactor1, RIGHT, buff=0.1).align_to(parity_check_matrix, UP + DOWN)
        transmitted_vector1 = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(equal1, RIGHT, buff=0.1).align_to(equal1, UP + DOWN)
        transmitted_vector1_tex = MathTex(r"\vec{t}").next_to(transmitted_vector1,UP).align_to(data_tex,DOWN)
        right_arrow1 = MathTex(r"\Rightarrow"
                        ).next_to(transmitted_vector1, RIGHT, buff=0.1).align_to(transmitted_vector1, UP + DOWN)
        parity_check_matrix1 = MathTex(r"""
            \begin{pmatrix}
            1 & 0 & 1 & 0 & 1 & 0 & 1 \\
            0 & 1 & 1 & 0 & 0 & 1 & 1 \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
            \end{pmatrix}
        """).scale(0.4).next_to(right_arrow1, RIGHT, buff=0.1).align_to(right_arrow1, UP + DOWN)
        transmitted_vector1s = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(parity_check_matrix1, RIGHT, buff=0.1)
        transmitted_vector1s_tex = MathTex(r"\vec{t'}").next_to(transmitted_vector1s,UP).align_to(data_tex,DOWN)
        parity_check_matrix1_tex = MathTex("\mathbf{H}").next_to(parity_check_matrix1,UP).align_to(data_tex,DOWN)
        equal2 = Tex("=").next_to(transmitted_vector1s, RIGHT, buff=0.1).align_to(parity_check_matrix1, UP + DOWN)
        syndrome1 =MathTex(r"""
            \begin{pmatrix}
            0 \\ 0 \\ 0
            \end{pmatrix}
        """).scale(0.4).next_to(equal2, RIGHT, buff=0.1)
        syndrome1_tex = MathTex(r"\vec{s}").next_to(syndrome1,UP).align_to(data_tex,DOWN)
        self.play(Write(data_vactor1),Write(data_tex))
        self.play(Write(parity_check_matrix),Write(parity_check_matrix_tex))
        self.play(Write(equal1))
        self.play(Write(transmitted_vector1),Write(transmitted_vector1_tex))
        self.play(Write(right_arrow1))
       ## self.play(Write(transmitted_vector1s),Write(transmitted_vector1s_tex))
        self.play(TransformMatchingTex(transmitted_vector1.copy(),transmitted_vector1s),Write(transmitted_vector1s_tex))
        self.play(Write(parity_check_matrix1),Write(parity_check_matrix1_tex))
        self.play(Write(equal2))
        self.play(Write(syndrome1),Write(syndrome1_tex))
        self.wait(2)
        
        starting_p_arrows= syndrome1.get_right()
        e_arrow1 = RIGHT +UP
        e_arrow2 = RIGHT +DOWN
        arrow1= Arrow(start = starting_p_arrows,end = e_arrow1, stroke_width= 5,color = GREEN)
        arrow2= Arrow(start = starting_p_arrows,end = e_arrow2, stroke_width= 5,color = RED)
        self.play(Write(arrow1)) ## later move write arrow2 to the section where the vector isnt good
        self.wait(1.5)

        ##GREEN ARROW SECTION##
        green_reconstructing_matrix = MathTex(
            r"\begin{pmatrix}"
            r"0 & 0 & 1 & 0 & 0 & 0 & 0 \\"
            r"0 & 0 & 0 & 0 & 1 & 0 & 0 \\"
            r"0 & 0 & 0 & 0 & 0 & 1 & 0 \\"
            r"0 & 0 & 0 & 0 & 0 & 0 & 1"
            r"\end{pmatrix}"
        ).scale(0.4).next_to(arrow1, RIGHT, buff=0.1).align_to(arrow1, UP + DOWN)
        green_transmitted_vector =MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(green_reconstructing_matrix, RIGHT, buff=0.1)
        green_transmitted_vector_tex = MathTex(r"\vec{t}").next_to(green_transmitted_vector,UP)
        green_reconstructing_matrix_tex = MathTex("\mathbf{R}").next_to(green_reconstructing_matrix,UP).align_to(green_transmitted_vector_tex,DOWN)
        green_equal = Tex("=").next_to(green_transmitted_vector, RIGHT, buff=0.1).align_to(green_reconstructing_matrix, UP + DOWN)
        green_final_vector =MathTex(r"""
            \begin{pmatrix}
            1 \\ 0 \\ 1 \\ 1 
            \end{pmatrix}
        """).scale(0.4).next_to(green_equal, RIGHT, buff=0.1)
        green_final_vector_tex = MathTex(r"\vec{d'}").next_to(green_final_vector,UP).align_to(green_transmitted_vector_tex,DOWN)
        self.play(TransformMatchingTex(transmitted_vector1s.copy(),green_transmitted_vector),Write(green_transmitted_vector_tex))
        self.play(Write(green_reconstructing_matrix),Write(green_reconstructing_matrix_tex))
        self.play(Write(green_equal),TransformMatchingTex(VGroup(green_transmitted_vector.copy(),green_reconstructing_matrix.copy()),green_final_vector),Write(green_final_vector_tex))
        self.wait(1)


        #RED ARROW SELECTION
        red_transmitted_vector1s = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 1 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).move_to(transmitted_vector1s.get_center())
        red_transmitted_vector1s[0][14].set_color(RED) 
        red_syndrome1 =MathTex(r"""
            \begin{pmatrix}
            1 \\ 0 \\ 1
            \end{pmatrix}
        """).scale(0.4).move_to(syndrome1.get_center())
        red_syndrome1[0][2].set_color(RED) 
        red_syndrome1[0][4].set_color(RED)
        self.play(FadeOut(green_transmitted_vector),FadeOut(green_transmitted_vector_tex)
        ,FadeOut(green_equal),FadeOut(green_final_vector),FadeOut(green_final_vector_tex)
        ,FadeOut(green_reconstructing_matrix),FadeOut(green_reconstructing_matrix_tex))
        self.play(Transform(transmitted_vector1s,red_transmitted_vector1s),Indicate(red_transmitted_vector1s))
        self.play(Transform(syndrome1,red_syndrome1))
        self.wait(1)
        self.play(Transform(arrow1,arrow2))
        red_transmitted_vector1s_corrupted = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 1 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(arrow2, RIGHT, buff=0.1).align_to(arrow2, UP + DOWN).shift(DOWN)
        red_transmitted_vector1s_corrupted[0][14].set_color(RED)
        red_transmitted_vector1s_corrupted_tex = MathTex(r"\vec{t'}").next_to(red_transmitted_vector1s_corrupted,UP)
        red_right_arrow =  MathTex(r"\Rightarrow"
                        ).next_to(red_transmitted_vector1s_corrupted, RIGHT, buff=0.1).align_to(red_transmitted_vector1s_corrupted, UP + DOWN)
        red_reconstructing_matrix = MathTex(
            r"\begin{pmatrix}"
            r"0 & 0 & 1 & 0 & 0 & 0 & 0 \\"
            r"0 & 0 & 0 & 0 & 1 & 0 & 0 \\"
            r"0 & 0 & 0 & 0 & 0 & 1 & 0 \\"
            r"0 & 0 & 0 & 0 & 0 & 0 & 1"
            r"\end{pmatrix}"
        ).scale(0.4).next_to(red_right_arrow, RIGHT, buff=0.1)
        red_transmitted_vector1s_fixed = MathTex(r"""
            \begin{pmatrix}
            0 \\ 1 \\ 1 \\ 0 \\ 0 \\1 \\ 1
            \end{pmatrix}
        """).scale(0.4).next_to(red_reconstructing_matrix, RIGHT, buff=0.1)
        red_transmitted_vector1s_fixed[0][14].set_color(GREEN)
        red_transmitted_vector1s_fixed_tex = MathTex(r"\vec{t}").next_to(red_transmitted_vector1s_fixed,UP)
        red_reconstructing_matrix_tex = MathTex("\mathbf{R}").next_to(red_reconstructing_matrix,UP).align_to(red_transmitted_vector1s_corrupted_tex,DOWN)
        red_equal = Tex("=").next_to(red_transmitted_vector1s_fixed, RIGHT, buff=0.1).align_to(red_reconstructing_matrix, UP + DOWN)
        red_final_vector =MathTex(r"""
            \begin{pmatrix}
            1 \\ 0 \\ 1 \\ 1 
            \end{pmatrix}
        """).scale(0.4).next_to(red_equal, RIGHT, buff=0.1)
        red_final_vector_tex = MathTex(r"\vec{d'}").next_to(red_final_vector,UP).align_to(red_transmitted_vector1s_corrupted_tex,DOWN)
###
        self.play(TransformMatchingTex(transmitted_vector1s.copy(),red_transmitted_vector1s_corrupted),Write(red_transmitted_vector1s_corrupted_tex))
        self.wait(1)
        self.play(Indicate(red_syndrome1))
        self.play(Write(red_right_arrow),Write(red_transmitted_vector1s_fixed),Write(red_transmitted_vector1s_fixed_tex))
        self.play(Write(red_reconstructing_matrix),Write(red_reconstructing_matrix_tex))
        self.play(Write(red_equal),TransformMatchingTex(VGroup(red_transmitted_vector1s_fixed.copy(),red_reconstructing_matrix.copy()),red_final_vector),Write(red_final_vector_tex))
        self.wait(2)
