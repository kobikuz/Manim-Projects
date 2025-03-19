from manim import *

class FiniteFieldPolynomialsAnimation(Scene):
    def construct(self):
        # Introductory Texts (kept as Tex because they are partly text)
        intro_title = Tex(r"Finite Field Polynomials", font_size=60)
        intro_text = Tex(
            r"Let's pick a fixed $k$ and list all the polynomials obtained from",
            r"vectors of length $k$ over a finite field.",
            font_size=36,
        ).next_to(intro_title, DOWN)
        choice = Tex(
            r"Choose: $k=3$ (degree $2$ polynomials) and finite field $\mathbb{F}_2=\{0,1\}$",
            font_size=36,
        ).next_to(intro_text, DOWN, buff=0.5)
        vector_poly = Tex(
            r"A vector $\vec{v}=[a_0,a_1,a_2]$ corresponds to",
            r"$f(x)=a_0+a_1x+a_2x^2$, with each $a_i\in\{0,1\}$",
            font_size=36,
        ).next_to(choice, DOWN, buff=0.5)
        count = Tex(
            r"Since there are 3 coefficients and each can be 0 or 1,",
            r"we have $2^3=8$ polynomials.",
            font_size=36,
        ).next_to(vector_poly, DOWN, buff=0.5)
        
        # Show the introductory texts sequentially.
        self.play(Write(intro_title))
        self.wait(1)
        self.play(Write(intro_text))
        self.wait(1)
        self.play(Write(choice))
        self.wait(1)
        self.play(Write(vector_poly))
        self.wait(1)
        self.play(Write(count))
        self.wait(2)
        
        # Fade out all the text before starting the individual animations.
        self.play(FadeOut(VGroup(intro_title, intro_text, choice, vector_poly, count)))
        self.wait(1)
        
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
        pair_spacing = 1  # vertical space between pairs

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
                pair_group.next_to(all_pairs, DOWN, aligned_edge=LEFT, buff=pair_spacing)
            else:
                pair_group.to_edge(UP, buff=1)
            
            # Animate the creation of the vector.
            self.play(Write(vec_text), run_time=0.8)
            # Animate drawing the arrow.
            self.play(Create(arrow), run_time=0.8)
            # Animate the polynomial appearing via a TransformFromCopy from the vector.
            self.play(TransformFromCopy(vec_text, poly_text), run_time=1)
            self.wait(0.5)
            
            # Add the current pair to the group.
            all_pairs.add(pair_group)
        
        self.wait(3)
        
        # Fade out all the pairs.
        self.play(FadeOut(all_pairs), run_time=2)
        self.wait(1)
