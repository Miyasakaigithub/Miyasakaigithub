import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import ArtistAnimation
from matplotlib import animation
from PIL import Image,ImageFilter

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import surf2stl
import pyvista as pv

i=1
load_file = np.loadtxt("plot2_Th226_hitaisyou_v3")
x = load_file[(i)*200+1:(i)*200+200, 0]
y = load_file[(i)*200+1:(i)*200+200, 1]
for i2 in range(6):
    for i3 in range(len(x)-1):
        x = np.insert(x,[2*i3+1],[(x[2*i3]+x[2*i3+1])/2])
        y = np.insert(y,[2*i3+1],[(y[2*i3]+y[2*i3+1])/2])
X,Y = np.meshgrid(x,y)
#Z = np.nan_to_num((y*y-Y*Y)**0.5,nan=0.12349E-08)
Z = (y*y-Y*Y)**0.5
X2=np.append(X, X, axis=0)
X3=np.append(X2, X, axis=0)
X4=np.append(X3, X, axis=0)
Y2=np.append(Y, -Y, axis=0)
Y3=np.append(Y2, Y, axis=0)
Y4=np.append(Y3, -Y, axis=0)
Z2=np.append(Z, Z, axis=0)
Z3=np.append(Z2, -Z, axis=0)
Z4=np.append(Z3, -Z, axis=0)

surf2stl.write('3d.stl', X4, Y4, Z4)

mesh = pv.read("3d.stl")
cpos = mesh.plot()
