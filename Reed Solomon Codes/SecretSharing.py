from manim import *
import numpy as np
from scipy.interpolate import lagrange

class SecretSharing(Scene):
    def func(self, x):
         return (x-2)**2*x**3*(x+1)-2

    def construct(self):
        func_tex = MathTex(r"f(x) = (x - 2)^2 \cdot x^3 \cdot (x + 1) - 2").scale(0.8).to_edge(UP)
        axes = Axes(
            x_range=(-1.1, 2.3),
            y_range=(-4, 2),
            axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 6, "include_ticks": False},
            y_axis_config={"stroke_width": 6, "include_ticks": False},
            tips=False
        ).scale(0.85)
        f = ParametricFunction(
            lambda t: axes.c2p(t, self.func(t)),
            t_range=(-1.1, 2.3), stroke_width=6, color=GREEN_C
        )
        f_c_d= DashedVMobject(f.copy())
        f_c = f.copy()
        self.play(Write(axes), Write(f))
        self.wait()
        offsets = [ 1.4 *LEFT+0.5*UP,
                    1.4 *LEFT+0.5*UP,
                    1.5 *LEFT+0.5*UP ,
                    1.5 *LEFT+0.5*UP ,
                    1.5*RIGHT+0.5*UP,
                    1.5*RIGHT+0.5*UP,
                    0,
                    1.25*LEFT+0.5*UP,
                    1.25*LEFT+0.5*UP,
                    1.1*UP,
                    0,
                    1.25*RIGHT+0.5*UP]
        x_vals = np.linspace(-1, 2.3, 10)
        # Assume self.func(x) returns a number when given a float x.
        y_vals = np.array([float(self.func(x)) for x in x_vals]) #10 points!
        # Keep the numeric y-values for plotting (do not format them here)
        coors = [(x_vals[j], y_vals[j]) for j in range(len(x_vals))]

        points = VGroup()
        labels = VGroup()

        def assign_dots(arr):
            point_arr = VGroup()
            label_arr = VGroup()
            for i, (x, y) in enumerate(arr):
                # Use the numeric y-value for positioning the dot.
                d = Dot(
                    axes.c2p(x, y),
                    radius=1 * DEFAULT_DOT_RADIUS, color=BLUE_C
                )
                # Format y to 2 decimal places for the label text.
                t = Tex(f"({x}, {format(y, '.2f')})")
                t.next_to(d, DOWN)
           #     t.shift(offsets[i])
                point_arr.add(d)
                label_arr.add(t)
            return point_arr, label_arr

        points, labels = assign_dots(coors)
        self.play(Write(points), run_time=2)
        self.wait()
        diss_indexes = [[3,5,8,2,4,6],[1,3,4,6,8],[1,2,6,7]]
        x_remaining1 = np.array([x_vals[i] for i in range(10) if i not in [3,5,8,2,4,6]])
        y_remaining1 = np.array([y_vals[i] for i in range(10) if i not in [3,5,8,2,4,6]])
        poly1 = lagrange(x_remaining1, y_remaining1)
        x_remaining2 = np.array([x_vals[i] for i in range(10) if i not in [1,3,4,6,8]])
        y_remaining2 = np.array([y_vals[i] for i in range(10) if i not in [1,3,4,6,8]])
        poly2 = lagrange(x_remaining2, y_remaining2)
        x_remaining3 = np.array([x_vals[i] for i in range(10) if i not in [1,2,6,7]])
        y_remaining3 = np.array([y_vals[i] for i in range(10) if i not in [1,2,6,7]])
        poly3 = lagrange(x_remaining3, y_remaining3)
        x_remaining4 = np.array([x_vals[i] for i in range(10) if i not in [2,4,7]])
        y_remaining4 = np.array([y_vals[i] for i in range(10) if i not in [2,4,7]])
        poly4 = lagrange(x_remaining4, y_remaining4)
        def f1(x):
            return poly1(x)
        def f2(x):
            return poly2(x)
        def f3(x):
            return poly3(x)
        def f4(x):
            return poly4(x)
        funcs = [f1, f2,f3]
        graphs = [ParametricFunction(
                lambda t: axes.c2p(t, funcs(t)),
                t_range=(-1, 2.3),
                stroke_width=6,
                color = RED_B
                ) for funcs in funcs]
        diss_indexes4 = [2,4,7]
        points_4 = VGroup(*[points[j] for j in range(len(points)) if j not in diss_indexes4])
        points_4_a = VGroup(*[points[j] for j in diss_indexes4])
        self.play(TransformMatchingShapes(f,f_c_d),FadeOut(f),run_time=2)
        for i in range(len(diss_indexes)):
            group2 = VGroup(*[points[j] for j in range(len(points)) if j not in diss_indexes[i]])
            group = VGroup(*[points[j] for j in diss_indexes[i]])
            self.play(Indicate(group2))
            self.wait()
            self.play(FadeOut(group))
            self.wait(1)
            self.play(Write(graphs[i]), run_time=2)
            self.wait(1)
            self.play(Wiggle(graphs[i]))
            self.wait(1)
            self.play(FadeOut(graphs[i]) )
            self.play(FadeIn(group))

        graph_f4 = ParametricFunction(
                lambda t: axes.c2p(t,f4(t)),
                t_range=(-1.1, 2.3),
                stroke_width=6,
                color = GREEN
                ) 
        self.wait(1)
        self.play(FadeIn(func_tex))
        self.wait(0.5)
        self.play(Indicate(func_tex))
        self.wait(1.5)
        self.play(Indicate(VGroup(*points_4)))
        self.wait()
        self.play(FadeOut(points_4_a))
        self.play(Write(graph_f4), run_time = 2)
        self.wait(1)
        self.play(Circumscribe(graph_f4),FadeIn(points_4_a))
        self.wait(2)
        self.play(FadeOut(graph_f4))
        self.wait(2)

        x_vals2 = np.linspace(-1, 2.3, 23)
        # Assume self.func(x) returns a number when given a float x.
        y_vals2 = np.array([float(self.func(x)) for x in x_vals2]) #15 points!
        # Keep the numeric y-values for plotting (do not format them here)
        coors2 = [(x_vals2[j], y_vals2[j]) for j in range(len(x_vals2))]
        points2, labels2 = assign_dots(coors2)
        self.play(FadeOut(points),FadeIn(points2), run_time=2)
        self.wait(1)
        self.play(Write(f),run_time= 1)
        self.wait(2)
        self.play(Circumscribe(f))
        



