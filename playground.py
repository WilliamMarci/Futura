from distutils.util import run_2to3
from pdb import run
from tkinter import MOVETO
from turtle import circle, width
from manim import *
import numpy as np 
import math as m


class PlayGround(Scene):
    def construct(self):
        plane=NumberPlane()
        self.add(plane)
        square = Square(color=BLUE,fill_opacity=0.5).shift(RIGHT*2)
        text = Text("x=\ny=", font="Times New Roman").scale(0.75)
        
        labelx = DecimalNumber()
        labely = DecimalNumber()

        def update_func(mob):
            mob.next_to(square, RIGHT)
        text.add_updater(update_func)

        def square_center(i):
            def inner(mob):
                mob.set_value(square.get_center()[i])
                mob.next_to(text, RIGHT+DOWN*0.5*i+0.5*UP)
            return inner
        
        labelx.add_updater(square_center(0))
        labely.add_updater(square_center(1))
 
        
        circle = Circle(2).set_opacity(0)
        self.play(Create(square))
        self.play(Create(text))
        self.play(Create(labelx))
        self.play(Create(labely))
        self.add(circle)

        self.play(MoveAlongPath(square, circle), run_time=5, rate_func=linear)

        # self.wait(1)

        # def dot_position(mobject):
        #     mobject.set_value(dot.get_center()[0])
        #     mobject.next_to(dot)

        # dot = Dot(RIGHT*3)
        # label = DecimalNumber()
        # label.add_updater(dot_position)
        # self.add(dot, label)

        # self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))

class CurveCatch(Scene):
    def construct(self):
        dot_a=Dot(LEFT*3+UP*3)
        dot_b=Dot(LEFT*3+DOWN*3)
        dot_c=Dot(RIGHT*3+DOWN*3)
        dot_d=Dot(RIGHT*3+UP*3)

        def update_dot(target):
            def anime(mob,dt):
                mob.shift((target.get_center()-mob.get_center())*2*dt)
            return anime

        dot_a.add_updater(update_dot(dot_b))
        dot_b.add_updater(update_dot(dot_c))
        dot_c.add_updater(update_dot(dot_d))
        dot_d.add_updater(update_dot(dot_a))

        self.add(dot_a,dot_b,dot_c,dot_d)
        self.wait(5)

class Multiplication(Scene):
    def construct(self):
        circle = Circle(radius=2).set_color(WHITE)
        self.play(Create(circle))
        n=128
        k1=2.5
        k2=1
        v=k1/k2
        lineGroup=Group()
        for i in range(2*n):
            point1=Point(np.array([2*m.cos(2*m.pi/n*i),2*m.sin(2*m.pi/n*i),0]))
            point2=Point(np.array([2*m.cos(2*m.pi*v/n*i),2*m.sin(2*m.pi*v/n*i),0]))
            line=Line(point1,point2).set_color(WHITE).set_stroke(width=0.5)
            lineGroup.add(line)
            # self.play(Create(line),run_time=0.1)
        self.play(*[Create(mob) for mob in lineGroup],run_time=1)
    
        # self.add(circle,lineGroup)

class VectorFieldwithTime(Scene):

    def construct(self):
        # def update_func(vectorField):
        def electricFieldwithTime(t):
            def electricField(pos):
                NOZERO=0.0001
                elc=normalize(pos-t*LEFT)/(np.linalg.norm(pos-t*LEFT)+NOZERO)**2
                return elc
            return electricField
        t=0
        dotCharge=Dot(LEFT+0.5*DOWN)
        vectorField=ArrowVectorField(electricFieldwithTime(t))
        def animField(mob,dt):
            nonlocal t
            t=t+dt
            mob.become(ArrowVectorField(electricFieldwithTime(t)))
        # vectorField.become
        #the dot nudges the vector field

        vectorField.add_updater(animField)
        dotCharge.add_updater(vectorField.get_nudge_updater())
        
        self.add(vectorField,dotCharge)
        self.wait(5)

