from manim import *

A_AQUA = "#8dd3c7"
A_YELLOW = YELLOW_B
A_LAVENDER = "#bebada"
A_RED = "#fb8072"
A_BLUE = "#80b1d3"
A_ORANGE = "#fdb462"
A_GREEN = GREEN_A
A_GREY = "#d9d9d9"
A_VIOLET = "#bc80bd"
A_UNKA = "#ccebc5"
A_UNKB = "#ffed6f"

class NumberSquare(VGroup):
    def __init__(self, number, color=RED, opacity=0.5, num_scale=3, side_length=2, square_kwargs={}, tex_kwargs={}, *args, **kwargs):
        VGroup.__init__(self, *args, **kwargs)

        self.sq = Square(side_length=side_length, fill_color=color,
                         fill_opacity=opacity, **square_kwargs)
        self.num = Tex(str(number), **tex_kwargs)
        self.num.scale(num_scale)

        self.add(self.sq, self.num)


class LabelledNumberSquare(NumberSquare):
    def __init__(self, *args, **kwargs):
        NumberSquare.__init__(self, *args, **kwargs)


class RSCodes(Scene):
    def construct(self):
        shades = ["#fc998e", "#fb8d80", "#fb8072", "#e27367", "#c9665b"]
        numbers = [2, 4, 3, 1, "?", "?"]
        numbers2 = [2, 4, 3, 1, 0, "?"]

        r1 = Rectangle(height=2.5, width=2.5).to_edge(LEFT).shift(0.3*RIGHT)
        r2 = Rectangle(height=2.5, width=2.5).to_edge(RIGHT).shift(0.3*LEFT)

        tt1 = Tex("Alice").move_to(r1).shift(2 * DOWN)
        tt2 = Tex("Bob").move_to(r2).shift(2 * DOWN)

        c = [2, 4, 0, 4, 1, 3]

        s = VGroup()
        for i in range(4):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1.5, num_scale=2)
            s.add(s_i.shift(2*i * RIGHT))
        s.center()

        self.play(Write(s))
        self.play(Write(r1), Write(tt1), Write(r2), Write(tt2))
        self.wait()

        s2 = VGroup()
        for i in range(6):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s2.add(s_i.shift(1.25*i * RIGHT))
        s2.center()

        b1 = Brace(s2[-2:])
        t1 = MathTex("k = 2", tex_to_color_map={
                        "k": YELLOW, "2": A_ORANGE})
        t1.scale(1.5)
        t1.next_to(b1, DOWN)

        self.play(ReplacementTransform(s, s2[:7]), Write(s2[7:]))
        self.play(GrowFromCenter(b1), Write(t1))
        self.wait()

        labels = VGroup()
        for i, obj in enumerate(s2):
            t = Tex(str(i+1), color=YELLOW_A)
            t.next_to(obj, UP)
            t.scale(1.25)
            labels.add(t)
        labels.next_to(s2, UP)

        labels2 = VGroup()
        for i, obj in enumerate(s2):
            t = MathTex(f"m_{{{i+1}}}", tex_to_color_map={f"{i+1}": YELLOW_A})
            t.next_to(obj, UP)
            t.scale(1.25)
            labels2.add(t)
        labels2.shift(0.25 * UP)
        labels2_cp = labels2.copy()

        self.play(Write(labels))
        self.wait()

        self.play(Transform(labels, labels2))
        self.wait()

        b2 = Brace(labels, UP)
        t2 = MathTex(r"p > m_{i}", tex_to_color_map={
                        "p": A_GREEN, "i": YELLOW}).next_to(b2,UP)

        self.play(GrowFromCenter(b2), Write(t2))
        self.wait()

        self.play(Uncreate(b2), Uncreate(t2))
        self.wait()

        s_cp, s_cp2 = s2.copy(), s2.copy()
        for i, x in enumerate(np.linspace(3, -3, 6)):
            s_cp[i].move_to(x * UP)
        s_cp.shift(2 * RIGHT)
        

        eqs = VGroup()
        for i, x in enumerate(np.linspace(3, -3, 6)):
            t = MathTex(f"f({i}) = m_{i+1}" if i < 4 else f"m_{i+1} = f({i})", tex_to_color_map={
                    "f": GREEN, "x": LIGHT_PINK,  str(i): YELLOW, str(i+1): YELLOW})
            t.move_to(x * UP)
            eqs.add(t)

        self.play(
            Uncreate(VGroup(b1, t1, labels[-1], labels[-2], r1, r2, tt1, tt2)))
        self.play(
            Transform(s2, s_cp),
            ReplacementTransform(
                labels[:-2],
                VGroup(*[eq[:] for eq in eqs])[:-2]
            )
        )
        self.wait()

        axes = Axes(
            x_range=(0, 4), y_range=(-2, 6),x_length=8, axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 3}, y_axis_config={"stroke_width": 3}
        )
        axes.scale(0.8).next_to(eqs,RIGHT).shift(3 * LEFT)

        curve = ParametricFunction(lambda t: axes.c2p(
            t, self.f(t)), t_range=(0, 5), color=A_GREEN)

        dots = VGroup()
        point_lbl = VGroup()

        for i in range(4):
            dots.add(Dot(axes.c2p(i, numbers[i]), color=A_GREEN))
            point_lbl.add(Tex(f"({i}, {numbers[i]})", tex_to_color_map={str(i): A_ORANGE, str(
                numbers[i]): A_ORANGE}).move_to(dots[i], DOWN))
        point_lbl.shift(0.75 * DOWN)
        eqs[-2:].shift(5 * LEFT)

        self.play(VGroup(*eqs[:-2], s2).animate.shift(5 * LEFT))  
        self.play(Write(axes))
        self.wait()

        self.play(TransformFromCopy(eqs[:-2], dots))
        self.play(Write(point_lbl))
        self.wait()

        self.bring_to_front(point_lbl)
        self.play(Write(curve))
        self.bring_to_front(point_lbl)
        self.wait()

        self.play(Write(eqs[-2:]))
        self.wait()
        start_of_eq =  VGroup(axes, curve, point_lbl, dots)
        self.play(FadeOut(start_of_eq))

        s_cp2.shift(2 * RIGHT)

        t1, t2 = Tex("f(4)"), Tex("f(5)")

        t1.move_to(s_cp2[-2])
        t2.move_to(s_cp2[-1])

        s_cp2[-1].remove(s_cp2[-1].num)
        s_cp2[-2].remove(s_cp2[-2].num)

        s_cp2[-1].num = t2
        s_cp2[-1].add(s_cp2[-1].num)

        s_cp2[-2].num = t1
        s_cp2[-2].add(s_cp2[-2].num)

        labels2_cp.shift(2 * RIGHT)

        l = Line(10 * UP, 10 * DOWN)
        l.shift(3 * LEFT)

        self.play(Transform(s2, s_cp2), Write(labels2_cp), Write(l))

        nr_1 = NumberSquare("?", A_GREY, side_length=1, num_scale=2).move_to(s2[1].get_center())
        nr_2 = NumberSquare("?", A_GREY, side_length=1, num_scale=2).move_to(s2[4].get_center())
        self.play(Transform(s2[1],nr_1),Transform(s2[4],nr_2))
        self.wait(2)
        
        self.wait()

        self.play(Uncreate(VGroup(eqs, l)))

        s_cp, labels2_cp2 = s2.copy(), labels2_cp.copy()

        for i, x in enumerate(np.linspace(3, -3, 6)):
            labels2_cp2[i].move_to(x * UP)
            s_cp[i].move_to(x * UP)

        s_cp.shift(6 * LEFT)
        labels2_cp2.shift(4.5 * LEFT)

        axes = Axes(
            x_range=(0, 6), y_range=(-2, 6),
            axis_config={"include_tip": False}, x_axis_config={"stroke_width": 3},
            y_axis_config={"stroke_width": 3}
        )
        axes.scale(0.85).next_to(labels2_cp2, RIGHT,buff= 0.1)
        Indicate

        

        self.play(
            Transform(s2, s_cp),
            Transform(labels2_cp, labels2_cp2)
        )

        coors = [(0, 2), (2, 3), (3, 1), (5, 2)]

        dots, labels = VGroup(), VGroup()
        for x, y in coors:
            dots.add(Dot(axes.c2p(x, y), color=A_GREEN))
            labels.add(
                Tex(f"({x}, {y})", tex_to_color_map={str(x): A_ORANGE, str(y): A_ORANGE}
                    ).move_to(dots[-1], DOWN).shift(0.25 * RIGHT))
        labels.shift(0.5 * RIGHT)

        curve = ParametricFunction(lambda t: axes.c2p(
            t, self.f(t)), t_range=(0, 6), color=A_GREEN)

        self.play(Write(axes))

        left = [0, 2, 3, 5]
        grp = VGroup(*self.get_indices(labels2_cp, left))

        self.play(TransformFromCopy(grp, dots))
        self.play(Write(labels))
        self.wait()

        self.play(Write(curve))
        self.bring_to_front(labels)

        x = ValueTracker(0)
        d = Dot(radius=2*DEFAULT_DOT_RADIUS, color=A_YELLOW)
        d.move_to(axes.c2p(x.get_value(), self.f(x.get_value())))

        def point_updater(point):
            new_point = point.move_to(
                axes.c2p(x.get_value(), self.f(x.get_value())))
            point.become(new_point)

        l1 = Line()

        def dash_updater_x(line):
            point = axes.c2p(x.get_value(), self.f(x.get_value()))
            new_line = Line(axes.c2p(0, self.f(x.get_value())),
                            point, stroke_opacity=0.5)
            line.become(new_line)
            self.bring_to_back(line)

        l2 = Line()

        def dash_updater_y(line):
            point = axes.c2p(x.get_value(), self.f(x.get_value()))
            new_line = Line(axes.c2p(x.get_value(), 0),
                            point, stroke_opacity=0.5)
            line.become(new_line)
            self.bring_to_back(line)

        self.play(Write(d))
        d.add_updater(point_updater)

        l1.add_updater(dash_updater_x)
        l2.add_updater(dash_updater_y)
        self.wait()

        lbl = Tex(f"(1, 4)", tex_to_color_map={"1": A_ORANGE, "4": A_ORANGE}).move_to(
            Point(axes.c2p(1, 4)), DOWN).shift(0.25 * UP).add_background_rectangle(buff=0.1)

        self.play(Indicate(VGroup(d, labels[0][1:])))
        self.play(TransformFromCopy(d, s_cp[0]))
        self.wait()

        self.play(x.animate.increment_value(1), run_time=3)  # ✅ Correct
        self.play(Write(lbl))
        self.play(Indicate(VGroup(d, lbl[1:])))

        
        dot_y_value = self.f(1)  # Get y value when x=1
        nr = NumberSquare(str(int(dot_y_value)), shades[c[1]], side_length=1, num_scale=1.5).move_to(s_cp[1])
        self.play(TransformFromCopy(d, nr),FadeOut(s2[1]))
        self.wait()

        self.play(x.animate.increment_value(1), run_time=3)  # ✅ Correct

        self.play(Indicate(VGroup(d, labels[1][1:])))
        self.play(TransformFromCopy(d, s_cp[2]))
        self.wait()

        self.play(x.animate.increment_value(1), run_time=3)  # ✅ Correct

        self.play(Indicate(VGroup(d, labels[2][1:])))
        self.play(TransformFromCopy(d, s_cp[3]))

        s = VGroup()
        for i in range(4):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s.add(s_i.shift(1.5*i * RIGHT))
        s.center()
        s.move_to(3 * UP)

        m = {"{5}": A_ORANGE, **{str(i): A_YELLOW for i in list(
            range(5)) + list(range(6, 10)) + [56]}, "f": A_GREEN}

        eq = MathTex(r"f(x) = 2x^3 + 2 \mod {{5}}", tex_to_color_map=m)
        eq.scale(1.5)
        eq.shift(1.5 * UP)

        eqs, eqs2 = VGroup(), VGroup()
        for i, y in enumerate(numbers[:-2]):
            mod_eq = MathTex(rf"f({i}) = {2*i**3 + 2} \mod {{5}}",
                         tex_to_color_map=m)
            mod_eq.scale(1.5)
            mod_eq.move_to(6 * LEFT, LEFT)
            mod_eq.shift(i * DOWN)
            eqs.add(mod_eq)

            mod_eq2 = MathTex(
                rf"f({i}) = {(2*i**3+2)%5} \mod {{5}}", tex_to_color_map=m)
            mod_eq2.scale(1.5)
            mod_eq2.move_to(6 * LEFT, LEFT)
            mod_eq2.shift(i * DOWN)
            eqs2.add(mod_eq2)
        s2[1] = nr
        remove_grp = VGroup(
            axes, d, curve, dots, lbl,
            labels2_cp2, labels, labels2_cp, s_cp, *s2[-2:],
            l1, l2)

        self.play(Uncreate(remove_grp))
        self.remove(*self.mobjects[:2])
        self.wait()
        s2[4] = NumberSquare(
                numbers[4], shades[c[4]], side_length=1, num_scale=1.5)
        self.play(Transform(s2[:-2], s))
        self.wait()

        self.play(Write(eq))
        self.wait()

        self.play(Write(eqs[0]))
        self.wait(1)

        self.play(Write(eqs[1]))
        self.wait(1)

        self.play(Write(eqs[2]))
        self.play(TransformMatchingTex(eqs[2], eqs2[2]))
        self.wait(1)

        self.play(Write(eqs[3]))
        self.play(TransformMatchingTex(eqs[3], eqs2[3]))
        self.wait(1)

        eqs_right1 = MathTex(r"f(4) = 0 \mod 5", tex_to_color_map={
                         "5": A_ORANGE, "0": A_YELLOW, "4": A_YELLOW, "f": A_GREEN})
        eqs_right1.scale(1.5)
        eqs_right1.move_to(1.5*RIGHT+1/2*LEFT, LEFT)

        eqs_right2 = MathTex(r"f(5) = 2 \mod {{5}}", tex_to_color_map={
                         r"5": A_YELLOW, "{5}": A_ORANGE, "2": A_YELLOW, "4": A_YELLOW, "f": A_GREEN})
        eqs_right2.scale(1.5)
        eqs_right2.move_to(1.5*RIGHT+1/2*LEFT + 1 * DOWN, LEFT)

        s_11 = VGroup()
        for i in range(5):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s_11.add(s_i.shift(1.5*i * RIGHT))
        s_11.center()
        s_11.shift(3 * UP)

        s = s2[:-2]
        self.play(Transform(s, s_11[:-1]), Write(s_11[-1]))
        self.wait()

        s_12 = NumberSquare(0, shades[c[4]], side_length=1, num_scale=1.5)
        s_12.move_to(s_11[-1])

        self.play(Write(eqs_right1))
        self.play(TransformFromCopy(eqs_right1[4], s_12), Uncreate(s_11[-1]))
        self.wait()

        s_21 = VGroup()
        for i in range(6):
            s_i = NumberSquare(
                numbers2[i], shades[c[i]], side_length=1, num_scale=1.5)
            s_21.add(s_i.shift(1.5*i * RIGHT))
        s_21.center()
        s_21.shift(3 * UP)

        s_22 = NumberSquare(2, shades[c[5]], side_length=1, num_scale=1.5)
        s_22.move_to(s_21[-1])

        self.play(
            Transform(s, s_21[:-2]),
            ApplyMethod(s_12.move_to, s_21[-2]),
            Write(s_21[-1])
        )
        self.wait()

        self.play(Write(eqs_right2))
        self.play(TransformFromCopy(eqs_right2[4], s_22), Uncreate(s_21[-1]))
        self.wait()

        self.play(FadeOut(eq))

        r1 = BackgroundRectangle(s_21[0], buff=0.15, fill_opacity=0.85)
        r2 = BackgroundRectangle(s_22, buff=0.15, fill_opacity=0.85)
        r3 = BackgroundRectangle(eqs[0], buff=0.15, fill_opacity=0.85)
        r4 = BackgroundRectangle(eqs_right2, buff=0.15, fill_opacity=0.85)

        self.play(Write(VGroup(r1, r3)))
        self.play(Write(VGroup(r2, r4)))
        self.wait()

        self.play(TransformFromCopy(VGroup(eqs[1:], eqs_right1), eq))
        self.wait()

        self.play(TransformFromCopy(eq, s_21[0]))
        self.play(Uncreate(r3))
        self.wait()

        self.embed()
        

    @staticmethod
    def get_indices(arr, indices):
        return [arr[i] for i in indices]
    
    @staticmethod
    def f(x):
        return 1/3 * x**3 - 5/2 * x**2 + 25/6 * x + 2