import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Create 3D scatter plot
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(df['X'], df['Y'], df['Z'])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()