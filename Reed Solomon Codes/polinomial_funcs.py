from manim import *

class polinom_2(Scene):
    def construct(self):
        # Define the vector to polynomial pairs.
        pairs = [
            (r"[0,0,0]", r"f(x)=0"),
            (r"[0,0,1]", r"f(x)=x^2"),
            (r"[0,1,0]", r"f(x)=x"),
            (r"[0,1,1]", r"f(x)=x+x^2"),
            (r"[1,0,0]", r"f(x)=1"),
            (r"[1,0,1]", r"f(x)=1+x^2"),
            (r"[1,1,0]", r"f(x)=1+x"),
            (r"[1,1,1]", r"f(x)=1+x+x^2"),
        ]
        
        # Create a VGroup to store all the pairs for later arrangement.
        all_pairs = VGroup()
        pair_spacing = 0.5  # vertical space between pairs

        # Loop through each pair, animate them, and arrange vertically.
        for i, (vec_str, poly_str) in enumerate(pairs):
            # Create vector text using MathTex for math mode.
            vec_text = MathTex(vec_str, font_size=48)
            # Create polynomial text using MathTex.
            poly_text = MathTex(poly_str, font_size=48)
            # Create an arrow.
            arrow = Arrow(start=ORIGIN, end=RIGHT, buff=0.1, color=WHITE)
            
            # Arrange the vector, arrow, and polynomial in a row.
            pair_group = VGroup(vec_text, arrow, poly_text).arrange(RIGHT, buff=0.5)
            
            # If not the first pair, position below the previous one.
            if all_pairs:
                pair_group.scale(0.8).next_to(all_pairs, DOWN, aligned_edge=LEFT, buff=pair_spacing)
            else:
                pair_group.scale(0.8).to_edge(UP, buff=0.5)
            
            # Animate the creation of the vector.
            self.play(Write(vec_text), run_time=0.8)
            # Animate drawing the arrow.
            self.play(Create(arrow), run_time=0.8)
            # Animate the polynomial appearing via a TransformFromCopy from the vector.
            self.play(TransformFromCopy(vec_text, poly_text), run_time=0.8)
            self.wait(0.8)
            
            # Add the current pair to the group.
            all_pairs.add(pair_group)
        
        self.wait(3)
        
        # Fade out all the pairs.
        self.play(FadeOut(all_pairs), run_time=2)
        self.wait(1)
