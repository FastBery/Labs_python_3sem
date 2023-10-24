import matplotlib.pyplot as plt
import numpy as np
N = 0
with open('data.dat', 'r') as f:
   for line in f:
    N += 1
N = int(N/2)
fig, axs = plt.subplots(nrows=int(N/2), ncols=2, dpi=100, figsize=(12, 9))

data = []

with open('data.dat', 'r') as f:
    data = [i.replace('\n','') for i in f.readlines()]

axs = axs.flatten()
maxy = 0
maxx = 0
minx = 0
miny = 0

for i in range(N):
    datax = [float(j) for j in data[2*i].split()]
    if(max(datax) > maxx):
       maxx = max(datax)
    if(min(datax) < minx):
       minx = min(datax)
    datay = [float(j) for j in data[2*i + 1].split()]
    if(max(datay) > maxy):
       maxy = max(datay)
    if(min(datay) < miny):
       miny = min(datay)
    Frame = 'Frame' + str(i)
    axs[i].plot(datax, datay)
    axs[i].set_title(Frame)

for i in axs:
    i.set_xlim(minx, maxx)
    i.set_ylim(miny, maxy)
    i.grid(linestyle='-')
    i.set_xticks(np.arange(minx, maxx, step=1))
    i.set_yticks(np.arange(-10.5, 12.5, step=1.5))

plt.subplots_adjust(wspace=0.2, hspace=0.4)
fig.savefig('Figuer.png', dpi=300)
plt.show()
