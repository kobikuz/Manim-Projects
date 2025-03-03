from manim import *

class Modulu(Scene):
   def construct(self):
        # 1. Display a number line from 0 to 9
        number_line = NumberLine(x_range=[0, 10, 1], length=10)
        labels = VGroup(*[
            MathTex(str(i)).next_to(number_line.n2p(i), DOWN)
            for i in range(11)
        ])
        
        self.play(Create(number_line), Write(labels))
        self.wait(2)
        
       
        
        # List of positions to move the dot to
        nums = [3, 5, 7]
        colors = [RED, GREEN, BLUE]
        nums_tex = Tex(r"[3,5,7]",tex_to_color_map = {
            "3": colors[0],
            "5": colors[1],
            "7": colors[2]
        }).to_edge(UP)
        self.play(Write(nums_tex))

        dots0 = []
        # Animate the dot moving to each position
        for i in range(3):
            position = ValueTracker(0)
            dot = Dot(color=colors[i], radius=2 * DEFAULT_DOT_RADIUS)
            dot.add_updater(lambda d, pos=position: d.move_to(number_line.n2p(pos.get_value())))
            self.add(dot)
            self.play(position.animate.set_value(nums[i]), run_time=1.5+0.25*i)
            self.wait(2)
            dot.clear_updaters()  # Freeze the dot's position
            dots0.append(dot)

        
        self.play(Uncreate(nums_tex),FadeOut(VGroup(dots0)))

        # 2. Highlight the "mod 10" behavior by wrapping around
        mod = 10
        nums2 = [3, 7, 12,  16]
        mod_text = Tex(r"Now with Mod 10").scale(0.9).to_edge(UP)
        colors2 = [RED, GREEN, BLUE, YELLOW]
        nums2_tex=  Tex("[3,7,12,16]",tex_to_color_map = {
            "3": colors2[0],
            "7": colors2[1],
            "12": colors2[2],
            "16": colors2[3]
        }).scale(0.9).next_to(mod_text,DOWN)
        self.play(Write(mod_text),Write(nums2_tex))

        dots = []
        for i in range(len(nums2)):
            position = ValueTracker(0)
            dot = Dot(color=colors2[i], radius=2 * DEFAULT_DOT_RADIUS)
            dot.add_updater(lambda d, pos=position: d.move_to(number_line.n2p(position.get_value())))
            self.add(dot)
            if nums2[i] <= 10:
                self.play(position.animate.set_value(nums2[i]), run_time=1.5+0.25*i)
                self.wait(2)
            else:
                # 1. Move to 10
                self.play(position.animate.set_value(10), run_time=2)
                self.play(Indicate(dot))
                self.wait(1)
                # 2. Create a new dot copy at 0 and transform the current dot into it
                new_dot = Dot(color=colors2[i], radius=2 * DEFAULT_DOT_RADIUS)
                position = ValueTracker(0)
                new_dot.add_updater(lambda d: d.move_to(number_line.n2p(position.get_value())))
                self.play(Transform(dot,new_dot))
                dots.append(dot)
                self.wait(1)
                
                # 3. Move to the modulo result smoothly
                mod_result = nums2[i] % 10
                self.play(position.animate.set_value(mod_result), run_time=1)
                self.wait(2)
            dot.clear_updaters()
            dots.append(dot)
            
            
        self.play(FadeOut(VGroup(dots)))
        

        
        # 3. Transform the line into a circle (modular arithmetic visualization)
        circle = Circle(radius=3, color=WHITE).scale(0.9).next_to(nums2_tex, DOWN)
        offset = 0.15
        circle_numbers = VGroup(*[
            MathTex(str(i)).move_to(
                circle.point_at_angle(i * TAU / mod +PI/2)
                + (circle.point_at_angle(i * TAU / mod+ PI/2) - circle.get_center()) * offset
            )
            for i in range(mod)
        ])

        # Animate the transformation of number line to circle with numbers sticking out
        self.play(Transform(number_line, circle), Transform(labels, circle_numbers),nums2_tex.animate.move_to(mod_text),FadeOut(mod_text))
        self.wait(1)

        # For each number, animate the dot moving along the circle.
        dots2= []
        for i in range(len(nums2)):
        # Create a ValueTracker that will drive the dot's movement along the circle.
        # The dot's angle on the circle is computed using (value % mod)
            position = ValueTracker(0)
            dot = Dot(color=colors2[i], radius=2 * DEFAULT_DOT_RADIUS)
            angle_offset = PI/2  # if your labels/circle were rotated by 90°
            dot.add_updater(lambda d, pos=position: d.move_to(
                circle.point_at_angle(angle_offset + (pos.get_value() % mod) * TAU / mod)
            ))
            self.add(dot)
            
            if nums2[i] <= mod:
                # For numbers within the modulus range, simply animate to that number.
                self.play(position.animate.set_value(nums2[i]), run_time=1.5 + 0.25 * i)
                self.wait(2)
            else:
                # For numbers greater than mod, we want the dot to continue moving counterclockwise.
                # For example, if nums2[i] is 12, then mod_result = 12 % 10 = 2,
                # but we want the ValueTracker to animate from 0 to 10 + 2 = 12, continuously.
                target = nums2[i]  # target is above mod, ensuring continuous motion
                self.play(position.animate.set_value(target), run_time=2+0.35*i)
                self.wait(2)
            dots2.append(dot)
        

        self.play(FadeOut(VGroup(dots2)))
        self.wait(1)
    
        