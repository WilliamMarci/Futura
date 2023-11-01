import math as m
import numpy as np
# import matplotlib.pyplot as plt
# rotate the vector by theta with the axis vector of rotation in 3D
def rotateVector(vector,theta,axis_vector):
    #caculate the vector after rotate
    #caculate the projection of vector on axis_vector
    z_component = np.dot(vector,axis_vector)/np.linalg.norm(axis_vector)
    i_vector = vector - z_component*axis_vector
    vector_rotate =m.cos(theta)*(i_vector-np.dot(i_vector,axis_vector)*axis_vector)+m.sin(theta)*np.cross(axis_vector,i_vector)+z_component*axis_vector
    return vector_rotate

#caculate the vector after reflact
#input the line direction and the normal vector and index of refraction
def reflactVector3D(line_vector,normal_vector,n1,n2):
    #dot product of two vector divid by the product of their length
    theta1 =m.acos(np.dot(line_vector,normal_vector)/(np.linalg.norm(line_vector)*np.linalg.norm(normal_vector)))
    if (m.sin(theta1)>n1/n2):
        return np.array([0,0,0])
    else:
        theta2 =m.asin( n1/n2*m.sin(theta1))
        #caculate the surface where ray and normal vector on it
        surface_normal_vector = np.cross(line_vector,normal_vector)/np.linalg.norm(np.cross(line_vector,normal_vector))
        #caculate the vector after reflact(by rotate the normal vector)
        normal_vector_rotate = rotateVector(-1*normal_vector,theta2,surface_normal_vector)
        return normal_vector_rotate
    
#input the line direction and the normal vector and index of refraction in 2D
def reflactVector2D(line_vector2D,normal_vector2D,n1,n2):
    #dot product of two vector divid by the product of their length
    line_vector = np.array([line_vector2D[0],line_vector2D[1],0])
    normal_vector = np.array([normal_vector2D[0],normal_vector2D[1],0])
    theta1 =m.acos(np.dot(line_vector,normal_vector)/(np.linalg.norm(line_vector)*np.linalg.norm(normal_vector)))
    if (m.sin(theta1)>n1/n2):
        return np.array([0,0])
    else:
        theta2 =m.asin( n1/n2*m.sin(theta1))
        #caculate the surface where ray and normal vector on it
        surface_normal_vector = np.cross(line_vector,normal_vector)/np.linalg.norm(np.cross(line_vector,normal_vector))
        #caculate the vector after reflact(by rotate the normal vector)
        normal_vector_rotate = rotateVector(-1*normal_vector,theta2,surface_normal_vector)
        normal_vector_2D = np.array([normal_vector_rotate[0],normal_vector_rotate[1]])
        return normal_vector_2D

#计算两线交点


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
