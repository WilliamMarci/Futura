import numpy as np
import math as m
import matplotlib.pyplot as plt
from lib.morevec import *
# test the reflactVector2D function
'''
theta=m.pi/6
rayIn=np.array([m.sin(theta),-m.cos(theta)])
normalVector=np.array([0,1])
rayOut=reflactVector2D(rayIn,normalVector,1,1.5)
print(rayOut)
plt.plot([-rayIn[0],0],[-rayIn[1],0])
plt.plot([0,rayOut[0]],[0,rayOut[1]])
plt.plot([0,normalVector[0]],[0,normalVector[1]])
plt.axis('equal')
plt.show()
'''
# test the reflactVector3D function
'''
theta=m.asin(1/1.5)-m.pi/100
# rayIn=np.array([m.sin(m.pi/3),0,-m.cos(m.pi/3)])
rayIn=np.array([m.sin(theta),0,-m.cos(theta)])
normalVector=np.array([0,0,1])
rayOut=reflactVector(rayIn,normalVector,1,1.5)
print(rayOut)
fig=plt.figure()
ax3d=fig.add_subplot(projection='3d')

ax3d.plot([-rayIn[0],0],[-rayIn[1],0],[-rayIn[2],0])
ax3d.plot([0,rayOut[0]],[0,rayOut[1]],[0,rayOut[2]])
ax3d.plot([0,normalVector[0]],[0,normalVector[1]],[0,normalVector[2]])
X,Y=np.meshgrid(np.arange(-1,1,0.1),np.arange(-1,1,0.1))
Z=(normalVector[0]*X+normalVector[1]*Y)/normalVector[2]
ax3d.plot_surface(X,Y,Z,alpha=0.5)
plt.show()
'''

rayIn=np.array([m.sin(m.pi/3),-m.cos(m.pi/3),0])
normalVector=np.array([0,1,0])
rayOut=reflectVector(rayIn,normalVector)
plt.plot([-rayIn[0],0],[-rayIn[1],0])
plt.plot([0,rayOut[0]],[0,rayOut[1]])
plt.plot([0,normalVector[0]],[0,normalVector[1]])
plt.axis('equal')
plt.show()

