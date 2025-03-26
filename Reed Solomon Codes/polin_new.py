from manim import *
        #CHECK INDEXES
        #self.add(index_labels(vector_x[0]))
        #self.add(index_labels(new_vector_x[0]))
class polinom_1(Scene):
    def construct(self): 
        colors = [YELLOW,RED,BLUE,GREEN,ORANGE]   
        vector_x = MathTex(r"""
            \begin{pmatrix}
            a \\ b \\ c \\ d \\ e \\ .\\. 
            \end{pmatrix}
        """).to_edge(LEFT).shift(RIGHT*2)
        brace_1=Brace(vector_x,LEFT)
        brace_1_tex = MathTex("r").next_to(brace_1, LEFT)
        equation = MathTex(r"""ax^0+bx^1+cx^2+dx^3+ex^5+...""").next_to(vector_x, RIGHT).shift(RIGHT*2)
        eqs = [MathTex(r"""ax^0"""),MathTex(r"""bx^1"""),MathTex(r"""cx^2"""),MathTex(r"""dx^3"""),MathTex(r"""ex^4""")]
        self.play(Write(vector_x)) # LETS ASSUME WE HAVE A VECTOR X 
        self.wait(1)
        self.play(Write(brace_1),Write(brace_1_tex)) #with lenght r
        self.wait(1)
        ## indicate 8 9 10 11 12 for the vector x
        #indicate 0 for the eqs[i]
        for i,eq in enumerate(eqs):
            self.play(Indicate(vector_x[0][10+i],color=colors[i]),run_time=0.7)
            self.wait(0.2) #each element of the vector x is a coeeficient of the polynomial
        self.wait(1)
        for i,eq in enumerate(eqs):
            equation[0][4*i].set_color(colors[i])
            self.play(vector_x[0][10+i].animate.set_color(colors[i]),run_time=0.7)
            self.play(TransformFromCopy(vector_x[0][10+i],equation[0][4*i]))
            self.wait(0.1)
            self.play(Write(equation[0][4*i+1:4*i+4]))
        self.play(Write(equation[0][-3:]))
        self.wait(2)

    