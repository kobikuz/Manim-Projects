from manim import *

class LagrangeFormula(Scene):
    def construct(self):
        # The full LaTeX formula
        formula = MathTex(
            r"f(x) = \sum_{j=0}^{k} y_j \prod_{i \ne j} \frac{x - x_i}{x_j - x_i}"
        )

        # Display each part step-by-step
        self.play(Write(formula))  
        self.wait()
       # self.add(index_labels(formula[0]))
       # self.add(index_labels(formula[0]))
       # self.wait(2)

        self.play(Indicate(formula[0][7],scale_factor=2.5),run_time = 2)
        self.wait(1)
        self.play(Indicate(formula[0][9]),Indicate(formula[0][5],scale_factor=2.5),run_time = 2)
        self.wait(1)
        self.play(Indicate(formula[0][17],scale_factor=2),run_time = 2)
        self.play(Indicate(formula[0][17:21],scale_factor=1.5),run_time = 2.5)
        self.wait()
        self.play(Indicate(formula[0][22:27],scale_factor=1.5),run_time = 2)
        self.wait()
        self.play(Indicate(formula[0][12:17],scale_factor=1.5),run_time = 2)
        self.wait()
        self.play(Indicate(formula[0][10:12],scale_factor=1.5),run_time = 2)
        self.wait()
        self.play(Indicate(formula[0][5:10],scale_factor=1.5),run_time = 2)
        self.wait(3)
        """
        j
        0 , k-1
        x
        (x-xi)
        (xj-xi)
        prod
        yj
        sum
        """
        

        # Hold the result
        self.wait(2)