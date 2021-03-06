import numpy as np
import matplotlib.pyplot as plt
from gradsio import *

f = open('2008020100.grd', 'rb')
t = readgrads(f, 3, nv3d=6, nv2d=6, nx=192, ny=94, nz=64, endian='b')
f.close()

lon = np.arange(192+1) * 1.875
lat = np.array((
  -88.541962,
  -86.653148,
  -84.753236,
  -82.850762,
  -80.947352,
  -79.043484,
  -77.139357,
  -75.235053,
  -73.330653,
  -71.426184,
  -69.521661,
  -67.617097,
  -65.712512,
  -63.807894,
  -61.903261,
  -59.998608,
  -58.093949,
  -56.189275,
  -54.284602,
  -52.379915,
  -50.475217,
  -48.570520,
  -46.665816,
  -44.761109,
  -42.856398,
  -40.951687,
  -39.046969,
  -37.142248,
  -35.237526,
  -33.332805,
  -31.428084,
  -29.523356,
  -27.618628,
  -25.713900,
  -23.809170,
  -21.904439,
  -19.999707,
  -18.094976,
  -16.190243,
  -14.285511,
  -12.380777,
  -10.476043,
   -8.571308,
   -6.666573,
   -4.761838,
   -2.857103,
   -0.952368,
    0.952368,
    2.857103,
    4.761838,
    6.666573,
    8.571308,
   10.476043,
   12.380777,
   14.285511,
   16.190243,
   18.094976,
   19.999707,
   21.904439,
   23.809170,
   25.713900,
   27.618628,
   29.523356,
   31.428084,
   33.332805,
   35.237526,
   37.142248,
   39.046969,
   40.951687,
   42.856398,
   44.761109,
   46.665816,
   48.570520,
   50.475217,
   52.379915,
   54.284602,
   56.189275,
   58.093949,
   59.998608,
   61.903261,
   63.807894,
   65.712512,
   67.617097,
   69.521661,
   71.426184,
   73.330653,
   75.235053,
   77.139357,
   79.043484,
   80.947352,
   82.850762,
   84.753236,
   86.653148,
   88.541962))

data = np.hstack((t[0,:,:], t[0,:,0:1])) - 273.15
[lonall, latall] = np.meshgrid(lon, lat)
mymapf = plt.contourf(lonall, latall, data, levels=list(range(-100,50,10)), cmap=plt.cm.Reds)
mymap = plt.contour(lonall, latall, data, levels=list(range(-100,50,10)), colors='k')

plt.clabel(mymap, fontsize=10, fmt='%.0f')
plt.axis([0, 360, -90, 90])
plt.xlabel('Longitude (degree)')
plt.ylabel('Latitude (degree)')
plt.colorbar(mymapf, orientation='horizontal')
plt.savefig('testplot.png', dpi=300)
plt.savefig('testplot.eps')

plt.show()
