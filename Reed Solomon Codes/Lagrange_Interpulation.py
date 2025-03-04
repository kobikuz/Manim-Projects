from manim import *
from copy import deepcopy 
class Lagrange_Interpulation(Scene):
    def func(self, x):
        return -x**2 + 4*x - 1

    def construct(self):
        x_vals = [1, 3, 4]
        y_vals = [2, 2, -1]
        coors = [(x_vals[i], y_vals[i]) for i in range(3)]

        colors = [RED, YELLOW_C, BLUE]

        curve_kwargs = {
            "stroke_width": 6
        }

        axes = Axes(
            x_range=(0, 5),
            y_range=(-3, 3),
            axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 6},
            y_axis_config={"stroke_width": 6}
        )

        points = VGroup()
        labels = VGroup()
        offsets = [0.75 * RIGHT, 0.75 * LEFT, 0.75 * LEFT]

        for i, (x, y) in enumerate(coors):
            d = Dot(
                axes.c2p(x, y),
                radius=1 * DEFAULT_DOT_RADIUS, color=GREEN
            )

            t = Tex(f"({x}, {y})")
            t.next_to(d, DOWN)
            t.shift(offsets[i])

            points.add(d)
            labels.add(t)

        labels_cp = labels.copy()


        c = ParametricFunction(
            lambda t: axes.c2p(t, self.func(t)),
            t_range=(0, 4.25), stroke_width=6, color=GREEN_A
        )

        eq = MathTex("p(x) = -x^2 + 4x - 1").scale(1.5).shift(3.25 * UP)
        eq_f = eq.copy()
        grp = VGroup(axes, c, points, labels)

        self.play(Write(axes), Write(points), Write(labels))
        self.wait()

        self.play(Write(c))
        self.wait()

        self.play(ApplyMethod(grp.shift, 0.5 * DOWN))
        self.play(Write(eq))
        self.wait()

        self.play(FadeOut(VGroup(eq, c)))

        def l1(x): return (x-3)*(x-4)/6
        l1_c = ParametricFunction(
            lambda t: axes.c2p(t, l1(t)),
            t_range=(0, 5), color=colors[0], stroke_width=6
        )
        l1_cp = l1_c.copy()
        p2l1_cp = l1_c.copy()
        def l2(x): return (x-1)*(x-4)/-2
        l2_c = ParametricFunction(
            lambda t: axes.c2p(t, l2(t)),
            t_range=(0, 5), color=colors[1], stroke_width=6
        )
        l2_cp = l2_c.copy()
        p2l2_cp = l2_c.copy()
        def l3(x): return (x-1)*(x-3)/3
        l3_c = ParametricFunction(
            lambda t: axes.c2p(t, l3(t)),
            t_range=(0, 5), color=colors[2], stroke_width=6
        )
        l3_cp = l3_c.copy()
        p2l3_cp = l2_c.copy()
        l_c = VGroup(l1_c, l2_c, l3_c)
        l_cp = l_c.copy()

        self.play(
            Write(l_c),
        )
        self.wait()
    ## DEFINING FUNCTIONS
        def hide_all_but(curr_idx):
            anims = []
            for i in range(3):
                if i != curr_idx:
                    anims.append(FadeOut(l_c[i]))  # Completely fade out other graphs
            self.play(*anims)

        def show_all():
            anims = [FadeIn(l_c[i]) for i in range(3)]  # Restore graphs
            self.play(*anims)

        def one_hot(x_val, curve_index):
            return 1 if x_val in x_vals and x_val == x_vals[curve_index] else 0

        def show_curve(curve_index):
            hide_all_but(curve_index)  # Hide other graphs

            points_0 = VGroup()
            for x in x_vals:
                points_0.add(
                    Dot(axes.c2p(x, one_hot(x, curve_index)), radius=0.1, color=colors[curve_index])
                )

            labels_0 = VGroup()
            for i in range(3):
                labels_0.add(
                    Tex(f"({x_vals[i]}, {one_hot(x_vals[i], curve_index)})").next_to(points_0[i], UP)
                )

            self.play(Write(points_0), Transform(labels, labels_0))
            self.wait()

            self.play(Indicate(labels[curve_index]))
            self.wait()

            self.play(
                Transform(labels, labels_cp),
                Uncreate(points_0)  # Remove points smoothly
            )
            show_all()  # Restore all graphs

            self.wait()

    ## RUNNING THE FUNCTIONS
        show_curve(0)
        show_curve(1)
        show_curve(2)

##new part
        def p2_l1(x): return (x-3)*(x-4)
        p2_l1_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l1(t)),
            t_range=(1.7, 5), color=colors[0], stroke_width=6
        )
        def p2_l3(x): return (x-1)*(x-3)
        p2_l3_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l3(t)),
            t_range=(0, 4), color=colors[2], stroke_width=6
        )
        def p2_l2(x): return (x-1)*(x-4)
        p2_l2_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l2(t)),
            t_range=(0.2, 4.75), color=colors[1], stroke_width=6
        )
        
        self.play(Uncreate(l_c))
        self.wait()
        eq10 = MathTex(
            r"l_1(x) = (x-3) (x-4)"
        )
        eq12 = MathTex(
            r"l_3(x) = (x-1) (x-3)"
        )
        eq11 = MathTex(
            r"l_2(x) = (x-1) (x-4)"
        )
        eq10.scale(0.7).to_corner(UL).set_color(colors[0])
        eq11.scale(0.7).next_to(eq10,RIGHT,buff = 0.5).set_color(colors[1])
        eq12.scale(0.7).next_to(eq11,RIGHT,buff = 0.5).set_color(colors[2])
        
        eq10s = MathTex(
            r"l_1(x) = (1-3) (1-4)"
        )
        eq12s = MathTex(
            r"l_3(x) = (4-1) (4-3)"
        )
        eq11s = MathTex(
            r"l_2(x) = (3-1) (3-4)"
        )
        eq10s.scale(0.7).move_to(eq10).set_color(colors[0])
        eq11s.scale(0.7).move_to(eq11).set_color(colors[1])
        eq12s.scale(0.7).move_to(eq12).set_color(colors[2])

        eq20 = MathTex(
        r"l_1(x) = \frac{1}{6} (x - 3) (x - 4)"
        ).set_color(colors[0])
        eq22 = MathTex(
        r"l_3(x) = \frac{1}{3} (x - 1) (x - 3)"  
        ).set_color(colors[2])
        eq21 = MathTex(
        r"l_2(x) = -\frac{1}{2} (x - 1) (x - 4)"
        ).set_color(colors[1])
        def p2_l1_1(x): return (x-3)*(x-4)/6
        p2_l1_1_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l1_1(t)),
            t_range=(0, 5), color=colors[0], stroke_width=6
        )
        def p2_l3_1(x): return (x-1)*(x-4)/-2
        p2_l2_1_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l3_1(t)),
            t_range=(0, 5), color=colors[1], stroke_width=6
        )
        def p2_l2_1(x): return (x-1)*(x-3)/3
        p2_l3_1_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l2_1(t)),
            t_range=(0, 5), color=colors[2], stroke_width=6
        )
        eq20.scale(0.7).move_to(eq10)
        eq21.scale(0.7).move_to(eq11)
        eq22.scale(0.7).move_to(eq12)
        
        eq_arr_result_1 = MathTex(r" =6")
        eq_arr_result_2 = MathTex(r" =-2")
        eq_arr_result_3 = MathTex(r" =3")

        #mult by y
        eq20f = MathTex(
        r"l_1(x) = \frac{1}{3} (x - 3) (x - 4)"
        ).set_color(colors[0])
        eq22f = MathTex(
        r"l_3(x) = -\frac{1}{3} (x - 1) (x - 3)"  
        ).set_color(colors[2])
        eq21f = MathTex(
        r"l_2(x) =  -(x - 1) (x - 4)"
        ).set_color(colors[1])

        def p2_l1_1f(x): return (x-3)*(x-4)/3
        p2_l1_1f_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l1_1f(t)),
            t_range=(0.3, 5), color=colors[0], stroke_width=6
        )
        def p2_l3_1f(x): return (-1)*(x-1)*(x-4)
        p2_l2_1f_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l3_1f(t)),
            t_range=(0.5, 4.75), color=colors[1], stroke_width=6
        )
        def p2_l2_1f(x): return (x-1)*(x-3)/(-3)
        p2_l3_1f_c = ParametricFunction(
            lambda t: axes.c2p(t, p2_l2_1f(t)),
            t_range=(0.1, 5), color=colors[2], stroke_width=6
        )
        
        eq20f.scale(0.7).move_to(eq10)
        eq21f.scale(0.7).move_to(eq11)
        eq22f.scale(0.7).move_to(eq12)
        
        eq_arr_first = [eq10,eq11,eq12]
        p2_funcs0 = [p2_l1_c,p2_l2_c,p2_l3_c]
        eq_arr_second = [eq10s,eq11s,eq12s]
        eq_arr_result = [eq_arr_result_1,eq_arr_result_2,eq_arr_result_3]
        p2_funcs1 = [p2_l1_1_c,p2_l2_1_c,p2_l3_1_c]
        eq_after_x_tex = [eq20,eq21,eq22]
        eq_mult_y = [p2_l1_1f_c,p2_l2_1f_c,p2_l3_1f_c]
        eq_mult_y_tex = [eq20f,eq21f,eq22f]
        

        for i in range(3):
            self.play(Write(eq_arr_first[i]))
            self.play(Write(p2_funcs0[i]))## basic func
            self.wait(0.5)
            self.play(Indicate(labels[i][0][1]))
            self.wait(0.5)
            self.play(Transform(eq_arr_first[i],eq_arr_second[i]),run_time = 1)## calculating
            self.wait(0.5)
            self.play(Write(eq_arr_result[i].next_to(eq_arr_first[i],RIGHT).set_color(colors[i])))## result
            self.wait(0.5)
            self.play(TransformMatchingTex(eq_arr_first[i], eq_after_x_tex[i]),  # Morph equation text
                AnimationGroup(
                    eq_arr_result[i].animate.shift(2*LEFT+0.5*DOWN ).set_opacity(0),  # Move left & fade out
                    lag_ratio=0  # Ensures both happen simultaneously
                ),run_time = 1)
            self.wait(0.5)
            self.play(
                Transform(p2_funcs0[i], p2_funcs1[i])  # Transform the function curve
                )
            self.wait(1)
            if i==2:
                self.play(Indicate(labels[i][0][3:5]))
                self.play(TransformMatchingTex(eq_after_x_tex[i],eq_mult_y_tex[i]))
                self.wait(0.5)
                self.play(Transform(p2_funcs0[i],eq_mult_y[i]))
            else: 
                self.play(Indicate(labels[i][0][3]))
                self.play(TransformMatchingTex(eq_after_x_tex[i],eq_mult_y_tex[i]))
                self.wait(0.5)
                self.play(Transform(p2_funcs0[i],eq_mult_y[i]))
                
            self.wait(1)

        self.wait(1.5)
        all_curves = VGroup(p2_funcs0[0],p2_funcs0[1],p2_funcs0[2])
        all_eq = VGroup(eq_mult_y_tex[0],eq_mult_y_tex[1],eq_mult_y_tex[2])
        self.play(Transform(all_curves,c),TransformMatchingTex(all_eq,eq_f),run_time = 2)
        self.wait(1.5)