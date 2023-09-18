from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        circle.generate_target()
        circle.target.shift(2*RIGHT+UP)

        self.add(circle)
        self.play(Create(circle))
        self.play(MoveToTarget(circle))