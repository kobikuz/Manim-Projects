from manim import *
import numpy as np  # used later for np.linspace
import numpy as np
from scipy.interpolate import lagrange

# ----------------------------------------------------------
# Colour palette
# ----------------------------------------------------------
A_AQUA     = "#8dd3c7"
A_YELLOW   = YELLOW_B
A_LAVENDER = "#bebada"
A_RED      = "#fb8072"
A_BLUE     = "#80b1d3"
A_ORANGE   = "#fdb462"
A_GREEN    = GREEN_A
A_GREY     = "#d9d9d9"
A_VIOLET   = "#bc80bd"
A_UNKA     = "#ccebc5"
A_UNKB     = "#ffed6f"

# ----------------------------------------------------------
# Helper classes
# ----------------------------------------------------------
class NumberSquare(VGroup):
    def __init__(
        self, number, color=RED, opacity=0.5,
        num_scale=3, side_length=2,
        square_kwargs={}, tex_kwargs={}, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.sq = Square(
            side_length=side_length,
            fill_color=color, fill_opacity=opacity,
            **square_kwargs,
        )
        self.num = Tex(str(number), **tex_kwargs).scale(num_scale)
        self.add(self.sq, self.num)


# ----------------------------------------------------------
# Main Scene
# ----------------------------------------------------------
class RSCodes(Scene):
    # polynomial used throughout
    @staticmethod
    def f(x):
        return 1 * x**3 +0 * x**2 + 1 * x + 3
    @staticmethod
    def p(x):
        return (1/15)*x**3 - (7/6)*x**2 + (107/30)*x + 3

    def construct(self):
        shades = ["#fc998e", "#fb8d80", "#fb8072", "#e27367", "#c9665b"]
        # ====================================================
        # 0.  Draw axes & polynomial + formula
        # ====================================================
        axes = Axes(
            x_range=(0, 6), y_range=(0, 226),
            axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 3},
            y_axis_config={"stroke_width": 3, "include_ticks"  : False}
        ).scale(0.7)

        axes_n = Axes(
            x_range=(0, 6), y_range=(-3, 6),
            axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 3},
            y_axis_config={"stroke_width": 3}
        ).scale(0.7)

        graph = axes.plot(self.f, x_range=(0, 6), color=A_GREEN)
        graph2 =axes_n.plot(self.p, x_range=(0, 6), color=A_GREEN)

        func_tex = MathTex(
            r"f(x)=x^{3}+x+3"
        ).next_to(axes, UP, buff=0.5)

       
        #self.play(Write(func_tex))
        #self.wait(1.5)
         # ----------------------------------------------------
        # Split formula into pieces → green coefficient squares
        # ----------------------------------------------------
        coeff_tex = VGroup(
            MathTex(r"\dfrac13"),
            MathTex(r"-\dfrac52"),
            MathTex(r"\dfrac{25}{6}"),
            MathTex(r"2"),
        ).arrange(RIGHT, buff=1.2).move_to(func_tex)

        coeff_tex.set_opacity(0)   # fully invisible
        self.add(coeff_tex)
        coeff_vals  = ["1", "0", "1", "3"]
        column_targets = VGroup()
        for val in coeff_vals:
            sq = NumberSquare(val, color=A_GREEN, side_length=1, num_scale=0.9)
            column_targets.add(sq)
        column_targets_copy= column_targets.copy()
        column_targets.arrange(DOWN, buff=0.25) \
                    .to_edge(LEFT, buff=1.0) \
                    .align_to(func_tex, UP).shift(1 * DOWN)


       # for tex_sym, target_sq in zip(coeff_tex, column_targets):
       #     self.play(TransformFromCopy(tex_sym, target_sq), run_time=0.85)
       #     self.wait(0.5)
        for coeff in column_targets:
            self.play(FadeIn(coeff), run_time=0.5)
            self.wait(0.75)
        self.wait(2)

        self.play(TransformFromCopy(VGroup(column_targets),func_tex))
        self.wait(2)
        g= DashedVMobject(graph)
        self.play(Create(axes), TransformFromCopy(func_tex,g))
        self.wait(3)
        self.play(Transform(axes,axes_n),Transform(g,DashedVMobject(graph2)))
        self.wait(3)

        # ----------------------------------------------------
        # ❶  Sampling demo — 7 dots fly into a right-side column
        #      x = 0,1,2,3,4,5,6   →   f(x) = [2,4,3,1,0,2,9]
        # ----------------------------------------------------
        demo_xs     = list(range(7))
        demo_vals   = [3, 5, 6, 5, 1, 0, 1]           # ▸▸ new list
        demo_index  = [1, 2, 3, 2, 4, 0, 4]           # colour indices
        demo_shades = ["#fc998e", "#fb8d80", "#fb8072",
                    "#e27367", "#c9665b"]        # same palette


        dots        = VGroup()
        demo_column = VGroup()

        # 1) create and show dots on the graph
        for x_val in demo_xs:
            d = Dot(axes_n.c2p(x_val, self.p(x_val)), color=A_ORANGE)
            dots.add(d)
            self.play(GrowFromCenter(d), run_time=0.3)
            self.wait(0.3)

        # 2) build the target column of NumberSquares
        for val, idx in zip(demo_vals, demo_index):
            sq = NumberSquare(val, demo_shades[idx],
                            side_length=0.75, num_scale=1)
            demo_column.add(sq)

        demo_column.arrange(DOWN, buff=0.25) \
                .to_edge(RIGHT, buff=1.0) \
                .align_to(func_tex, UP).shift(0.25 * DOWN)

        # 3) fly each dot into its square’s slot, one by one
        for dot, square in zip(dots, demo_column):
            self.play(TransformFromCopy(dot, square), run_time=0.85)
            self.wait(0.5)

        self.wait(1)
        self.play(Indicate(column_targets, color =None,scale_factor=1.2))
        self.wait(2)
        self.play(Indicate(demo_column, color =None,scale_factor=1.1))
        self.wait(2)
        # remove axes & graph and dots
        self.play(FadeOut(VGroup(axes,g,dots,func_tex,column_targets)))

        # ====================================================
        # 1.  Begin original long animation
        # ====================================================

        numbers  = [3, 5, 6, 5, "?", "?"]             # ▸▸ new
        numbers2 = [3, 5, 6, 5, 1, "?"]               # ▸▸ new
        c        = [1, 2, 3, 2, 4, 0]                 # ▸▸ new

        r1 = Rectangle(height=2.5, width=2.5).to_edge(LEFT).shift(0.3*RIGHT)
        r2 = Rectangle(height=2.5, width=2.5).to_edge(RIGHT).shift(0.3*LEFT)
        tt1 = Tex("Alice").move_to(r1).shift(2 * DOWN)
        tt2 = Tex("Bob").move_to(r2).shift(2 * DOWN)

        # ---- first four NumberSquares ----------------------
        d_c =demo_column.copy()
        s = d_c.arrange(RIGHT, buff=0.25) 

        # morph column → first four data squares
        self.play(Transform(demo_column,s))
        self.play(Create(r1), Write(tt1), Create(r2), Write(tt2))




        self.play(ReplacementTransform(s, s[:8]), Write(s[8:]),
                  FadeOut(demo_column))
        self.wait()
        s2= s
        
        labels = VGroup()
        for i, obj in enumerate(s2):
            t = Tex(str(i), color=YELLOW_A).scale(1.25)
            t.next_to(obj, UP)
            labels.add(t)
        labels.next_to(s2, UP)
        self.wait(1)
        labels2 = VGroup()
        for i, obj in enumerate(s2):
            t = MathTex(f"m_{{{i}}}",
                        tex_to_color_map={f"{i+1}": YELLOW_A}
                        ).scale(1.25)
            t.next_to(obj, UP)
            labels2.add(t)
        labels2.shift(0.25 * UP)
        labels2_cp = labels2.copy()
        """
        self.play(Write(labels))
        self.wait(2)
        self.play(Transform(labels, labels2))
        self.wait()

        b2 = Brace(labels, UP)
        t2 = MathTex(r"p > m_{i}").next_to(b2, UP)
        self.wait()
        t2_new = MathTex(r"p=7 > m_{i}").next_to(b2, UP)
        self.play(GrowFromCenter(b2), Write(t2))
        self.wait()
        self.play(Transform(t2, t2_new))
        self.play(FadeOut(b2), FadeOut(t2))
        self.wait(2)
        """
        self.play(Write(labels2))
        s_cp, s_cp2 = s2.copy(), s2.copy()

        self.play(Transform(s2, s_cp2))

        nr_1 = NumberSquare("?", A_GREY, side_length=0.75, num_scale=1
                           ).move_to(s2[1].get_center())
        nr_2 = NumberSquare("?", A_GREY, side_length=0.75, num_scale=1
                           ).move_to(s2[4].get_center())
        nr_3 = NumberSquare("?", A_GREY, side_length=0.75, num_scale=1
                           ).move_to(s2[-1].get_center())
        self.play(Transform(s2[1], nr_1), Transform(s2[4], nr_2),Transform(s2[-1], nr_3))
        self.wait(2)

        s_cp, labels2_cp2 = s2.copy(), labels2_cp.copy()
        for i, x in enumerate(np.linspace(3, -3, 7)):
            labels2_cp2[i].move_to(x * UP)
            s_cp[i].move_to(x * UP)
        s_cp.shift(6 * LEFT)
        labels2_cp2.shift(5 * LEFT)

        axes3 = Axes(                                 # vertical range 0–6
                x_range=(0, 6), y_range=(-3, 6),      # ▸▸ updated
                axis_config={"include_tip": False},
                x_axis_config={"stroke_width": 3},
                y_axis_config={"stroke_width": 3},
                ).scale(0.7).next_to(labels2_cp2, RIGHT, buff=1).shift(0.5 * DOWN)

        self.play(FadeOut(VGroup(r1,tt1,r2,tt2)),
            Transform(s2, s_cp),
            Transform(labels2, labels2_cp2)
        )

        coors = [(0, 3), (2, 6), (3, 5), (5, 0)]      
        dots, labels3 = VGroup(), VGroup()
        for x_val, y_val in coors:
            dots.add(Dot(axes3.c2p(x_val, y_val), color=A_GREEN))
            labels3.add(
                Tex(f"({x_val}, {y_val})",
                    tex_to_color_map={str(x_val): A_ORANGE,
                                      str(y_val): A_ORANGE})
                .move_to(dots[-1], DOWN).shift(0.25*RIGHT))
        labels3.shift(0.5 * RIGHT)

        xs = np.array([0, 2, 3, 5], dtype=float)
        ys = np.array([3, 6, 5, 0], dtype=float)          # f(x) mod 7

        poly = lagrange(xs, ys)                           # scipy returns a poly1d

        curve3 = ParametricFunction(                      # plot the interpolant
            lambda t: axes3.c2p(t, poly(t) ),          # keep values in GF(7)
            t_range=(0, 6),
            color=A_GREEN,
        )

        self.play(Write(axes3))
        grp = VGroup(*self.get_indices(labels2_cp2, [0, 2, 3, 5]))
        self.play(TransformFromCopy(grp, dots))
        self.play(Write(labels3), run_time =4)
        self.wait(2)
        c=DashedVMobject(curve3)
        self.play(Write(c))
        #self.bring_to_front(labels3)
        """
        x_tracker = ValueTracker(0)
        moving_dot = Dot(radius=2*DEFAULT_DOT_RADIUS, color=A_YELLOW)
        moving_dot.move_to(axes3.c2p(0, self.f(0)))

        def dot_updater(mobj):
            mobj.move_to(axes3.c2p(x_tracker.get_value(),
                                   self.f(x_tracker.get_value())))
        moving_dot.add_updater(dot_updater)
        self.play(Write(moving_dot))
        self.wait()

        l1, l2 = Line(), Line()

        def upd_x(line):
            p = axes3.c2p(x_tracker.get_value(), self.f(x_tracker.get_value()))
            line.become(Line(axes3.c2p(0,
                       self.f(x_tracker.get_value())), p, stroke_opacity=0.5))
            self.bring_to_back(line)

        def upd_y(line):
            p = axes3.c2p(x_tracker.get_value(), self.f(x_tracker.get_value()))
            line.become(Line(axes3.c2p(x_tracker.get_value(), 0),
                       p, stroke_opacity=0.5))
            self.bring_to_back(line)

        l1.add_updater(upd_x)
        l2.add_updater(upd_y)

        lbl = Tex("(1, 4)", tex_to_color_map={
                  "1": A_ORANGE, "4": A_ORANGE}
                  ).move_to(Point(axes3.c2p(1, 4)), DOWN
                  ).shift(0.25*UP).add_background_rectangle(buff=0.1)

        self.play(x_tracker.animate.set_value(1), run_time=3)
        self.play(Write(lbl))
        self.play(Indicate(VGroup(moving_dot, lbl[1:])))
        nr_val = self.f(1)
        nr = NumberSquare(str(int(nr_val)), shades[c[1]],
                          side_length=0.75, num_scale=1).move_to(s_cp[1])
        self.play(TransformFromCopy(moving_dot, nr), FadeOut(s2[1]))
        self.wait()

        self.play(x_tracker.animate.set_value(2), run_time=3)
        self.play(Indicate(VGroup(moving_dot, labels3[1][1:])))
        self.play(TransformFromCopy(moving_dot, s_cp[2]))
        self.wait()

        self.play(x_tracker.animate.set_value(3), run_time=3)
        self.play(Indicate(VGroup(moving_dot, labels3[2][1:])))
        self.play(TransformFromCopy(moving_dot, s_cp[3]))
        """
        func_tex2 = MathTex(
            r"f(x)=x^{3}+x+3").to_edge(UP)
        self.wait(2)
        self.play(TransformFromCopy(labels3,func_tex2))
        self.wait(2)
       # remove_grp = VGroup(
       #     axes3, moving_dot, curve3, dots, lbl,
       #     labels2, labels3, 
       #     s_cp[0], s_cp[2], s_cp[3], *s2[-3:],
       #     l1, l2)
        remove_grp = VGroup(
            axes3, c, dots,
           labels2, labels3, 
           s_cp[0], s_cp[2], s_cp[3], *s2[:]
           )
        column_targets_copy.arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=1)
        self.play(FadeOut(remove_grp), TransformFromCopy(func_tex2,column_targets_copy),
                  func_tex2.animate.center().shift(1*UP),
                  column_targets_copy.animate.center().shift(1*DOWN), run_time = 2)
        self.wait(2)
        self.play(FadeOut(func_tex2,column_targets_copy))
        self.wait(2)

    # ------------------------------------------------------
    # helper
    # ------------------------------------------------------
    @staticmethod
    def get_indices(arr, indices):
        return [arr[i] for i in indices]
