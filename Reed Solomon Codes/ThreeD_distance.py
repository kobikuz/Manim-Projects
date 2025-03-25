from manim import *
import numpy as np

class ThreeD_distance(ThreeDScene):
    def construct(self):
        # Set initial camera orientation to avoid abrupt movements
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES,zoom=0.60)

        # Create a 3D axes for reference
        axes = ThreeDAxes(x_range=(-20, 20), y_range=(-20, 20), z_range=(-20, 20)  )
          
        # Generate  3D points
        points = np.array([
                    [-2, -1,  0],
                    [-1,  1,  2] ,
                    [ 0,  0,  0],
                    [ 1,  2, -1],
                    [ 2, -2,  1],
                    [-2,  2, -2],
                    [ 2, -1,  2],
                    [-1, -2,  1],
                    [ 1,  0, -2],
                    [ 0,  1,  2]
                ])


        # Create a dot for each point in the field
        dots = VGroup(*[
            Dot3D(point=point, radius=0.5, color=BLUE)
            for point in points
        ])
        spheres = VGroup(*[
            Dot3D(point = point,radius=1).set_color(RED).set_opacity(0.3) 
            for point in points
        ])

        # Add axes and all points to the scene
        self.add(axes)
        self.wait(1.5)
        self.begin_ambient_camera_rotation(rate=0.1)
        anims1 =[]
        for dot in dots:
            anims1.append(FadeIn(dot))
        self.play(*anims1,run_time = 2)    
        self.wait(2)
        self.play(FadeIn(*spheres),run_time = 2)
        self.wait(5)
        anims =[]
        for dot in dots:
            anims.append(dot.animate.shift(dot.get_center()))
        for sphere in spheres:
            anims.append(sphere.animate.shift(sphere.get_center()).set_color(GREEN))
        self.play(*anims,run_time = 4,rate_func= smooth)
        # Begin ambient camera rotation after the scene is fully set up
        self.wait(5)
        self.stop_ambient_camera_rotation()
    """
    actually it works fine right now without the change of the points
    TO DO:
            1)need to chnage to this so that it works in correlation to the axes
            dots = VGroup(*[
            Dot3D(point=axes.c2p(*point), radius=0.5, color=BLUE)
            for point in points
            ])
            2) and then adjust the movement also
            3) THEN TO CHECK THAT THE DOTS ARENT ALLIGNING WITH ONE ANOTHER
  """