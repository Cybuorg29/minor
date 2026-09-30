import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x1 = np.array([1,2,3,4,5])
y1 = np.array([2,3,4,5,6])
z1 = np.array([3,4,5,6,7])

x2 = np.array([10,11,12,13,14])
y2 = np.array([20,21,22,23,24])
z2 = np.array([40,41,42,43,44])

x3 = np.array([100,200,300,400,500])
y3 = np.array([200,400,600,800,1000])
z3 = np.array([1,2,3,4,5])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, z1, c='r', marker='o', label='dataset1')
ax.scatter(x2, y2, z2, c='y', marker='^', label='dataset2')
ax.scatter(x3, y3, z3, c='g', marker='d', label='dataset3')
ax.legend()

plt.show()