import matplotlib.pyplot as plt
files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']

fig, axs = plt.subplots(nrows=5, ncols=1, dpi=40)
g = 0
for name in files:
    
    with open('./dead_moroz/' + name, 'r') as file:
        x, y = [], []
        N = int(file.readline())
        for i in range(N):
            data = [float(j) for j in file.readline().split()]
            x.append(data[0])
            y.append(data[1])
            axs[g].scatter(y, x)
        # axs[g].plot(x, y, labbel='first')
    g += 1

plt.show()