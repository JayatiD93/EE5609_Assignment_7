import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a,b,c,d = 0,3,-4,-7

x = np.linspace(-10,10,10)
y = np.linspace(-10,10,10)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax = plt.axes(projection='3d')

plt.rcParams['legend.fontsize'] = 10

X1,Y1 = np.meshgrid(x,y)
Z1 = (d - a*X1 - b*Y1) / c

surf1 = ax.plot_surface(X1, Y1, Z1,label="3y-4z+7=0")
surf1._facecolors2d=surf1._facecolors3d
surf1._edgecolors2d=surf1._edgecolors3d

m,n,o,p=0,4,3,0
X2,Y2 = np.meshgrid(x,y)
Z2 = (p-m*X2 -n*Y2)/o



surf2 = ax.plot_surface(X2, Y2, Z2,label="4y+3z=0")

surf2._facecolors2d=surf2._facecolors3d

surf2._edgecolors2d=surf2._edgecolors3d 
##############################################3


# Make a 3D quiver plot
#x, y, z = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
x, y, z = np.array([[-20,0,0],[0,-20,0],[0,0,-20]])
u, v, w = np.array([[40,0,0],[0,40,0],[0,0,40]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black")
#ax.quiver(x,y,z,arrow_length_ratio=0.1, color="black")
ax.grid(False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

z_point1 = (28/25)
x_point1 = 5
y_point1 = -21/25
ax.scatter3D(x_point1, y_point1, z_point1, color="black",label='$a(0,-0.84,1.12)$');

#ax.set_xlim(-10,10)
#ax.set_ylim(-10,10)
#ax.set_zlim(-10,10)
ax.legend(loc='upper left')
plt.show()

