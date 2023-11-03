 #use manim to draw a light ray after reflact
from manim import *
import math as m
import numpy as np
import matplotlib.pyplot as plt

import src.lib.morevec as mv

class Reflact(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.add_coordinates(range(-10, 11, 1), range(-10, 11, 1))
        glassWidth = 4
        glassHeight = 4
        glass = Rectangle(height=glassHeight, width=glassWidth*m.sqrt(2), color=BLUE, fill_opacity=0.2)

        glassSelf= Rectangle(height=glassHeight, width=glassWidth, color=BLUE, fill_opacity=0.2)
        text1=Text("Diagonal").scale(0.75).shift(3*UP+5*LEFT)
        text2=Text("Main").scale(0.75).shift(3*UP+5*LEFT)
        fomular=MathTex(r"\sin\theta_C=\frac{1}{n}").shift(1*DOWN+5*RIGHT)
        text_glass=Text("Glass").scale(0.75).shift(1.5*UP+1.5*RIGHT)
        text_air=Text("Air").scale(0.75).shift(2.5*UP+1.5*RIGHT)
        markGroop=Group(text_glass,text_air)
        self.add(plane)
        centerPoint=Dot(np.array([0,0,0]),color=YELLOW)
        self.play(Write(text1))
        self.play(Create(glass))
        self.play(*[Write(mob) for mob in markGroop])
        self.play(Create(centerPoint))

        rayInGroup=Group()
        rayOutGroup=Group()

        for i in range(-7, 8):
            # print(i)
            rayInVector=np.array([i/5,-1,0])
            # print(rayInVector)
            rayOutVector=mv.reflactVector3D(rayInVector, np.array([0,1,0]),1.5,1)
            # print(rayOutVector)
            rayIn=Line(start=np.array([0,0,0]),end=2*rayInVector,color=YELLOW)
            rayout=Line(start=rayInVector*2,end=2*rayInVector+10*rayOutVector,color=YELLOW)
            rayInGroup.add(rayIn)
            rayOutGroup.add(rayout)
        self.play(*[Create(mob) for mob in rayInGroup])
        self.play(*[Create(mob) for mob in rayOutGroup])
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in rayOutGroup])
        self.play(*[FadeOut(mob) for mob in rayInGroup])
        self.play(Transform(text1,text2))
        self.play(Transform(glass,glassSelf))

        rayInGroup=Group()
        rayOutGroup=Group()
        for i in range(-5, 6):
            # print(i)
            rayInVector=np.array([i/5,-1,0])
            # print(rayInVector)
            rayOutVector=mv.reflactVector3D(rayInVector, np.array([0,1,0]),1.5,1)
            # print(rayOutVector)
            rayIn=Line(start=np.array([0,0,0]),end=2*rayInVector,color=YELLOW)
            rayout=Line(start=rayInVector*2,end=2*rayInVector+10*rayOutVector,color=YELLOW)
            rayInGroup.add(rayIn)
            rayOutGroup.add(rayout)
        self.play(*[Create(mob) for mob in rayInGroup])
        self.play(*[Create(mob) for mob in rayOutGroup])
        #0.729728
        self.wait(1)
        fullReflectRayVector=np.array([m.tan(0.72972),-1,0])
        fullReflectRay=Line(start=np.array([0,0,0]),end=2*fullReflectRayVector,color=RED)
        fullReflectRayOutVector=mv.reflactVector3D(fullReflectRayVector, np.array([0,1,0]),1.5,1)
        fullReflectRayOut=Line(start=fullReflectRayVector*2,end=2*fullReflectRayVector+10*fullReflectRayOutVector,color=RED)
        self.play(Create(fomular))
        self.play(Create(fullReflectRay))
        self.play(Create(fullReflectRayOut))
        #animation



