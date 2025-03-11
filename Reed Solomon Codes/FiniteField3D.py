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
        # Start with a top view (camera looking straight down the z-axis).
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, zoom = 0.9)
        self.play(Create(axes))

        # Draw a circle in the xy-plane to represent the finite field.
        R = 3  # Radius of the field circle.
        field_circle = Circle(radius=R, color=YELLOW)
        self.play(Create(field_circle))
        
        # Define the finite field as 5 equally spaced points on the circle.
        angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
        field_points = [np.array([R * np.cos(theta), R * np.sin(theta), 0])
                        for theta in angles]
        field_dots = VGroup(*[Dot(point, color=YELLOW) for point in field_points])
        self.play(Create(field_dots))
        
        # Hold the top view for 5 seconds.
        self.wait(5)
        
        # Define the three functions.
        def f1(x):
            return (x - 3) * (x - 4) / 3

        def f2(x):
            return -1 * (x - 1) * (x - 4)

        def f3(x):
            return (x - 1) * (x - 3) / (-3)
        
        # Define x-domain boundaries.
        x_min_f1, x_max_f1 = 0.3, 5.0
        x_min_f23, x_max_f23 = 0.5, 4.75

        # Mapping functions:
        # For f1, map theta in [0, 2π] to x in [0.3, 5].
        def theta_to_x_f1(theta):
            return (theta / (2 * np.pi)) * (x_max_f1 - x_min_f1) + x_min_f1
        
        # For f2 and f3, now also use the full circle mapping:
        def theta_to_x_f23_full(theta):
            return (theta / (2 * np.pi)) * (x_max_f23 - x_min_f23) + x_min_f23

        # Helper function to create a smooth curve by sampling many points.
        def create_curve(func, t_range, mapping, color, stroke_width=6, num_points=500):
            t_start, t_end = t_range
            ts = np.linspace(t_start, t_end, num_points)
            points = [
                np.array([R * np.cos(t), R * np.sin(t), func(mapping(t))])
                for t in ts
            ]
            curve = VMobject()
            curve.set_points_as_corners(points)
            curve.set_color(color)
            curve.set_stroke(width=stroke_width)
            return curve

        # Create smooth curves for each function over the full circle.
        curve_f1 = create_curve(f1, (0, 2 * np.pi), theta_to_x_f1, BLUE)
        curve_f2 = create_curve(f2, (0, 2 * np.pi), theta_to_x_f23_full, RED)
        curve_f3 = create_curve(f3, (0, 2 * np.pi), theta_to_x_f23_full, GREEN)

        # Animate the curves appearing while the camera remains in top view.
        self.play(Create(curve_f1),run_time = 1.5)
        self.wait()
        self.play(Create(curve_f2),run_time = 1.5)
        self.wait()
        self.play(Create(curve_f3),run_time = 1.5)
        self.wait(5)
        
        # Transition the camera to an angled view.
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom = 0.75, run_time=4)
        # Begin ambient camera rotation to showcase the 3D structure.
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(15)
        
        # Define the Lagrange interpolation function.
        def lagrange_func(x):
            return -x**2 + 4*x - 1

        # Create a new curve for the Lagrange interpolation function using full circle mapping.
        curve_new = create_curve(lagrange_func, (0, 2 * np.pi), theta_to_x_f1, PURPLE)
        
        # Transform the current three curves into the new Lagrange interpolation curve.
        old_curves = VGroup(curve_f1, curve_f2, curve_f3)
        self.move_camera(zoom = 0.75,  run_time=4)
        self.play(Transform(old_curves, curve_new), run_time=4)
        
        # Continue ambient rotation for another 5 seconds to observe the new function.
        self.wait(7)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=0,  run_time=8)
        self.wait(2)