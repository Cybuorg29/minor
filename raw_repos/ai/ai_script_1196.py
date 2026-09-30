import stl
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create the mesh
data = stl.mesh.Mesh.from_file("house.stl")

# 3D plot
pyplot.figure()
ax = pyplot.axes(projection ='3d')
ax.add_collection3d(mplot3d.art3d.Poly3DCollection(data.vectors))

# Set size
scale = data.points.flatten(-1)
ax.auto_scale_xyz(scale, scale, scale)

# Save to file
pyplot.savefig('house.png', dpi = 600)