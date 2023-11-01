 #use manim to draw a light ray after reflact
from manim import *
import math as m
import numpy as np
import matplotlib.pyplot as plt

import morevec as mv

class Reflact(Scene):
    def construct(self):
        # set the surface
        # surface = Square()
        # surface.set_fill(BLUE, opacity=0.5)
        #set 2D ray in
        rayIn2D = np.array([m.sin(m.pi/6),-m.cos(m.pi/6)])
        #set 2D normal vector
        normalVector2D = np.array([0,1])
        #set 2D ray out
        rayOut2D = mv.reflactVector2D(rayIn2D,normalVector2D,1,1.5)
        
        #draw line of ray
        rayIn = Line(start=3*np.array([-rayIn2D[0],-rayIn2D[1],0]),end=np.array([0,0,0]),color=WHITE)
        rayOut = Line(start=np.array([0,0,0]),end=3*np.array([rayOut2D[0],rayOut2D[1],0]),color=WHITE  )
        #draw line of normal vector
        normalVector = Line(start=np.array([0,0,0]),end=3*np.array([0,1,0]),color=BLUE)
        #draw line of surface
        surfaceLine = Line(start=np.array([-10,0,0]),end=np.array([10,0,0]),color=YELLOW)
        
        #animation
        self.add(surfaceLine)
        self.play(Create(normalVector))
        self.play(Create(rayIn))
        self.play(Create(rayOut))


