from manim import *

class polinom_2(Scene):
    def construct(self):
        # Define the vector-to-polynomial pairs.
        pairs1 = [
            (r"[0,0,0]", r"f(x)=0"),
            (r"[0,0,1]", r"f(x)=x^2"),
            (r"[0,0,2]", r"f(x)=2x^2"),
            (r"[0,1,0]", r"f(x)=x"),
            (r"[0,1,1]", r"f(x)=x+x^2"),
            (r"[0,1,2]", r"f(x)=x+2x^2"),
            (r"[0,2,0]", r"f(x)=2x"),
            (r"[0,2,1]", r"f(x)=2x+x^2"),
            (r"[0,2,2]", r"f(x)=2x+2x^2")
        ]
        pairs2 = [
            (r"[1,0,0]", r"f(x)=1"),
            (r"[1,0,1]", r"f(x)=1+x^2"),
            (r"[1,0,2]", r"f(x)=1+2x^2"),
            (r"[1,1,0]", r"f(x)=1+x"),
            (r"[1,1,1]", r"f(x)=1+x+x^2"),
            (r"[1,1,2]", r"f(x)=1+x+2x^2"),
            (r"[1,2,0]", r"f(x)=1+2x"),
            (r"[1,2,1]", r"f(x)=1+2x+x^2"),
            (r"[1,2,2]", r"f(x)=1+2x+2x^2")
        ]
        pairs3 = [
            (r"[2,0,0]", r"f(x)=2"),
            (r"[2,0,1]", r"f(x)=2+x^2"),
            (r"[2,0,2]", r"f(x)=2+2x^2"),
            (r"[2,1,0]", r"f(x)=2+x"),
            (r"[2,1,1]", r"f(x)=2+x+x^2"),
            (r"[2,1,2]", r"f(x)=2+x+2x^2"),
            (r"[2,2,0]", r"f(x)=2+2x"),
            (r"[2,2,1]", r"f(x)=2+2x+x^2"),
            (r"[2,2,2]", r"f(x)=2+2x+2x^2")
        ]

        def build_column(pairs):
            """
            Create a VGroup containing the pairs arranged vertically.
            Each pair is a VGroup of the vector, arrow, and polynomial.
            Returns a VGroup.
            """
            column = VGroup()
            pair_spacing = 0.5  # vertical spacing between pairs

            # For each pair, create and group the mobjects.
            for vec_str, poly_str in pairs:
                # Create the vector and polynomial as MathTex objects.
                vec_text = MathTex(vec_str, font_size=42)
                poly_text = MathTex(poly_str, font_size=42)
                arrow = Arrow(start=ORIGIN, end=RIGHT, buff=0.05, color=WHITE)

                # Arrange them in a row.
                pair_group = VGroup(vec_text, arrow, poly_text).arrange(RIGHT, buff=0.03)
                # Optionally scale the group (here 0.8 as in your code).
                pair_group.scale(0.78)

                # If this column already has content, position this pair below the previous one.
                if column:
                    pair_group.next_to(column, DOWN, aligned_edge=LEFT, buff=pair_spacing)
                else:
                    # Place the first pair; its placement will be adjusted later.
                    pair_group.to_edge(UP, buff=0.3)

                column.add(pair_group)
            return column

        # Build the three columns.
        col1 = build_column(pairs1)
        col2 = build_column(pairs2)
        col3 = build_column(pairs3)

        # Position the columns.
        # col1 will be aligned to the left edge.
        col1.to_edge(LEFT)
        # Position col2 and col3 to the right of the previous column.
        col2.next_to(col1, RIGHT, buff=0.1)
        col3.next_to(col2, RIGHT, buff=0.1)

        
        self.play(Write(col1),run_time =8)
        self.play(Write(col2),run_time =8)
        self.play(Write(col3),run_time =8)

       
