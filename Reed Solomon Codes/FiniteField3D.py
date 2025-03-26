from manim import *
import numpy as np

class FiniteField3D(ThreeDScene):
    def construct(self):
        # Create 3D axes.
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-2, 7, 1],
        )
        # Start with a top view.
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, zoom=0.6) #zoom out more in the beggining so that the point be one on top of the other
        self.play(Create(axes))

        # Draw a circle in the xy-plane representing the finite field.
        R = 3  # Radius
        field_circle = Circle(radius=R, color=YELLOW)
        self.play(Create(field_circle))
        
        # Define the finite field as 11 equally spaced points on the circle.
        angles = np.linspace(0, 2 * np.pi, 11, endpoint=False)
        field_points = [np.array([R * np.cos(theta), R * np.sin(theta), 0])
                        for theta in angles]
        field_dots = VGroup(*[Dot3D(point, color=YELLOW, radius=0.1) for point in field_points])
        self.play(Create(field_dots))
        
        # Helper function to compute the 3D point on a graph for a given angle.
        def get_graph_point(func, mapping, theta):
            return np.array([R * np.cos(theta),
                             R * np.sin(theta),
                             func(mapping(theta))])
        
        # Define the x-domain boundaries.
        x_min_f1, x_max_f1 = 0.3, 5.0
        x_min_f23, x_max_f23 = 0.5, 4.75

        # Define the three functions.
        def f1(x):
            return (x - 3) * (x - 4) / 3

        def f2(x):
            return -1 * (x - 1) * (x - 4)

        def f3(x):
            return (x - 1) * (x - 3) / (-3)
        
        # Mapping functions.
        def theta_to_x_f1(theta):
            return (theta / (2 * np.pi)) * (x_max_f1 - x_min_f1) + x_min_f1
        
        def theta_to_x_f23_full(theta):
            return (theta / (2 * np.pi)) * (x_max_f23 - x_min_f23) + x_min_f23

        # Calculate and show 3D dots on each graph at the given angles.
        dots_f1 = VGroup(*[Dot3D(get_graph_point(f1, theta_to_x_f1, theta), color=BLUE, radius=0.1)
                           for theta in angles])
        dots_f2 = VGroup(*[Dot3D(get_graph_point(f2, theta_to_x_f23_full, theta), color=RED, radius=0.1)
                           for theta in angles])
        dots_f3 = VGroup(*[Dot3D(get_graph_point(f3, theta_to_x_f23_full, theta), color=GREEN, radius=0.1)
                           for theta in angles])
        self.wait(1)
        self.play(Create(dots_f1))
        self.wait(1)
        self.play(Create(dots_f2))
        self.wait(1)
        self.play(Create(dots_f3))
        self.wait(2)
        
        # Helper to create a smooth curve.
        def create_curve(func, t_range, mapping, color, stroke_width=6, num_points=500):
            t_start, t_end = t_range
            ts = np.linspace(t_start, t_end, num_points)
            points = [np.array([R * np.cos(t), R * np.sin(t), func(mapping(t))])
                      for t in ts]
            curve = VMobject()
            curve.set_points_as_corners(points)
            curve.set_color(color)
            curve.set_stroke(width=stroke_width)
            return curve

        # Create dashed curves for each function.
        curve_f1 = DashedVMobject(create_curve(f1, (0, 2 * np.pi), theta_to_x_f1, BLUE), num_dashes=40)
        curve_f2 = DashedVMobject(create_curve(f2, (0, 2 * np.pi), theta_to_x_f23_full, RED), num_dashes=40)
        curve_f3 = DashedVMobject(create_curve(f3, (0, 2 * np.pi), theta_to_x_f23_full, GREEN), num_dashes=40)
        
        # Transition the camera to an angled view.
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=0.75, run_time=4)
        
        # Write the dashed curves.
        self.play(Write(curve_f1), run_time=1.5)
        self.wait(1.5)
        self.play(Write(curve_f2), run_time=1.5)
        self.wait(1.5)
        self.play(Write(curve_f3), run_time=1.5)
        self.wait(1.5)
  
        # Ambient camera rotation to showcase the 3D structure.
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(15)
        
        # Define the Lagrange interpolation function.
        def lagrange_func(x):
            return -x**2 + 4*x - 1

        # Create a new dashed curve for the Lagrange interpolation.
        curve_new = DashedVMobject(create_curve(lagrange_func, (0, 2 * np.pi), theta_to_x_f1, PURPLE), num_dashes=40)
        dots_f4 = VGroup(*[
            Dot3D(get_graph_point(lagrange_func, theta_to_x_f1, theta), color=PURPLE, radius=0.1)
            for theta in angles
        ])

        # Group the old curves and points.


        self.move_camera(zoom=0.75, run_time=4)

        self.play(Transform(VGroup(dots_f1, dots_f2, dots_f3),dots_f4),
                  Transform(VGroup(curve_f1, curve_f2, curve_f3), curve_new), run_time=4)
        
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(mob) for mob in curve_new.submobjects], run_time=2)
        self.move_camera(phi=0, theta=0,zoom = 0.6, run_time=8)
        self.wait(2)
