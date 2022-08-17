import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import ArtistAnimation
from matplotlib import animation
from PIL import Image,ImageFilter
from scipy import interpolate

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

load_file = np.loadtxt("plot2_Th226_hitaisyou_v3")
x_all = load_file[:,0]
#x = load_file[0:200, 0]
#y = load_file[0:200, 1]

#N = int(int(len(x_all))/200)
N = 735# - 592 
# = 1# - 592 
print(N)

fig = plt.figure(figsize=(30,25))
ax = fig.add_subplot(111, projection='3d')
#ax.set_xlim(-30,30)
ax.set_xlim(-30,30)
#ax.set_ylim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
#ax.set_zlim(10,-10)

ax.grid(False)
ax.view_init(elev=50, azim=269.5)
ax.set_box_aspect((3,1,1))
ax.set_xticks([30,25,20,15,10,5,0,-5,-10,-15,-20,-25,-30])
ax.set_yticks([-10,-5,0,5,10])
#ax.invert_yaxis()
#ax.tick_params(direction='in',length=10.0,width=2.0,labelsize=40,pad = 30,colors='white',grid_color='black',grid_alpha=1.0)
ax.tick_params(labelsize=40,pad = 30)
ax.set_xlabel('x[fm]',labelpad=110,fontsize=40)
#ax.set_xlabel('x[fm]',labelpad=80,fontsize=40,fontweight='black')
ax.set_ylabel('y[fm]',labelpad=60,fontsize=40)
#ax.set_ylabel('y[fm]',labelpad=60,fontsize=40,fontweight='black')
print(ax.tick_params())

#ax.axis("off")
#面を直す
ax.xaxis.pane.set_edgecolor((1.0, 1.0, 1.0, 0.0))
ax.yaxis.pane.set_edgecolor((1.0, 1.0, 1.0, 0.0))
ax.zaxis.pane.set_edgecolor("blue")
ax.xaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.yaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.zaxis.pane.set_facecolor("blue")

#z軸をなくす目盛を
#ax.xaxis.set_major_locator(ticker.NullLocator())
#ax.xaxis.set_minor_locator(ticker.NullLocator())
#ax.yaxis.set_major_locator(ticker.NullLocator())
#ax.yaxis.set_minor_locator(ticker.NullLocator())
ax.zaxis.set_major_locator(ticker.NullLocator())
ax.zaxis.set_minor_locator(ticker.NullLocator())
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

ax.xaxis._axinfo['tick']['color']='r'
ax.yaxis._axinfo['tick']['color']='r'
#ax.zaxis._axinfo['tick']['color']='white'

#ax.tick_params(direction="in",length=0)
ax.xaxis._axinfo['tick']['inward_factor'] = 0
ax.xaxis._axinfo['tick']['outward_factor'] = 0.4
ax.yaxis._axinfo['tick']['inward_factor'] = 0
ax.yaxis._axinfo['tick']['outward_factor'] = 0.1
ax.zaxis._axinfo['tick']['inward_factor'] = 0
ax.zaxis._axinfo['tick']['outward_factor'] = 0.0

ax.w_xaxis.line.set_color('black')
ax.w_yaxis.line.set_color('black')
#ax.w_zaxis.line.set_color('red')

for i1 in range(N):
   #i=592 + i1
#   i=i1 + 212
    i=i1
    print(i)
    x = load_file[(i)*200+1:(i)*200+200, 0]
    y = load_file[(i)*200+1:(i)*200+200, 1]
    for i2 in range(2):
        for i3 in range(len(x)-1):
            x = np.insert(x,[2*i3+1],[(x[2*i3]+x[2*i3+1])/2])
            y = np.insert(y,[2*i3+1],[(y[2*i3]+y[2*i3+1])/2])
    X,Y = np.meshgrid(x,y)
#   Z = np.nan_to_num((y*y-Y*Y)**0.5,nan=0.12349E-08)
    Z = np.nan_to_num((y*y-Y*Y)**0.5,nan=0)
#   Z_fun = interpolate.interp2d(X,Y,Z,kind='cubic')
#   Z_f = Z_fun(x,y)
#   Z = (y*y-Y*Y)**0.5
    print("Zyade")
    print(Z)
    print("mae")
#   norm = plt.Normalize(vmin=-3*Z.max(), vmax=Z.max())
#   colors = plt.cm.gist_gray(norm(Z))
#   colors[Z == 0] = (0,0,0,0)
    print("ato")
    X1=[]
    Y1=[]
    Z1=[]
    X2=np.append(X, X, axis=0)
    X3=np.append(X2, X, axis=0)
    X4=np.append(X3, X, axis=0)
    Y2=np.append(Y, -Y, axis=0)
    Y3=np.append(Y2, Y, axis=0)
    Y4=np.append(Y3, -Y, axis=0)
    Z2=np.append(Z, Z, axis=0)
    Z3=np.append(Z2, -Z, axis=0)
    Z4=np.append(Z3, -Z, axis=0)
    norm = plt.Normalize(vmin=-Z4.max(), vmax=Z4.max())
#   norm = plt.Normalize(vmin=-2, vmax=12)
    colors = plt.cm.gist_gray(norm(Z4))
#   colors[Z4 == 0.12349E-08] = (1.0,1.0,1.0,0)
#   colors[Z4 == -0.12349E-08] = (1.0,1.0,1.0,0)
    colors[Z4 == 0] = (1.0,1.0,1.0,0)
    print(Z1)
    #ax.plot_surface(X4,Y4,Z4, facecolors=colors,rcount=101000,ccount=101000,shade=False,antialiased=True)
    ax.plot_surface(X4,Y4,Z4, facecolors=colors,rstride=1, cstride=1,shade=False,antialiased=True)

    plt.savefig('./hitaisyou4/'+str(i)+'.png')
    plt.cla()

    fig = plt.figure(figsize=(30,25))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-30,30)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)

    ax.grid(False)
    ax.view_init(elev=50, azim=269.5)
    ax.set_box_aspect((3,1,1))

    ax.set_xticks([-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30])
    #ax.invert_xaxis()
    #ax.set_xticks([30,25,20,15,10,5,0,-5,-10,-15,-20,-25,-30],fontweight='black')
    ax.set_yticks([-10,-5,0,5,10])
    #ax.tick_params(direction='in',length=10.0,width=2.0,labelsize=40,pad = 30,colors='white',grid_color='black',grid_alpha=1.0)
    ax.tick_params(labelsize=40,pad = 30)
    ax.set_xlabel('x[fm]',labelpad=110,fontsize=40)
    #ax.set_xlabel('x[fm]',labelpad=80,fontsize=40,fontweight='black')
    ax.set_ylabel('y[fm]',labelpad=60,fontsize=40)
    #ax.set_ylabel('y[fm]',labelpad=60,fontsize=40,fontweight='black')

    #ax.axis("off")
    #面を直す
    ax.xaxis.pane.set_edgecolor((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.pane.set_edgecolor((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.pane.set_edgecolor("blue")
    ax.xaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.pane.set_facecolor("blue")

    #z軸をなくす目盛を
    #ax.xaxis.set_major_locator(ticker.NullLocator())
    #ax.xaxis.set_minor_locator(ticker.NullLocator())
    #ax.yaxis.set_major_locator(ticker.NullLocator())
    #ax.yaxis.set_minor_locator(ticker.NullLocator())
    ax.zaxis.set_major_locator(ticker.NullLocator())
    ax.zaxis.set_minor_locator(ticker.NullLocator())
    ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

    ax.xaxis._axinfo['tick']['color']='r'
    ax.yaxis._axinfo['tick']['color']='r'
    #ax.zaxis._axinfo['tick']['color']='white'

    #ax.tick_params(direction="in",length=0)
    ax.xaxis._axinfo['tick']['inward_factor'] = 0
    ax.xaxis._axinfo['tick']['outward_factor'] = 0.4
    ax.yaxis._axinfo['tick']['inward_factor'] = 0
    ax.yaxis._axinfo['tick']['outward_factor'] = 0.1
    ax.zaxis._axinfo['tick']['inward_factor'] = 0
    ax.zaxis._axinfo['tick']['outward_factor'] = 0.0

    ax.w_xaxis.line.set_color('black')
    ax.w_yaxis.line.set_color('black')
    #ax.w_zaxis.line.set_color('red')
