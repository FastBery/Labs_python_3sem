import matplotlib.pyplot as plt
# files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']
files = ['00'+str(i)+'.dat' for i in range(1,6)]

# fig, axs = plt.subplots(nrows=1, ncols=1, dpi=100)
# g = 0

for name in files:
    fig, axs = plt.subplots(nrows=1, ncols=1, dpi=300)
    with open('./dead_moroz/' + name, 'r') as file:
        x, y = [], []
        N = int(file.readline())
        for i in range(N):
            data = [float(j) for j in file.readline().split()]
            x.append(data[0])
            y.append(data[1])
            
            axs.scatter(x, y, s=0.5)
            xleft, xright = axs.get_xlim()
            ybottom, ytop = axs.get_ylim()
            # axs.set_aspect(abs((xright-xleft)/(ybottom-ytop))*(9/16))
            axs.set_aspect('equal')
    fig.savefig(name.rstrip('.dat') + '.png', dpi=300)
# fig.suptitle("Several subplots", size=18)
# plt.set_aspect(16/9)
# plt.show()