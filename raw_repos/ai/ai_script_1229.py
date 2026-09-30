import os
import arcpy

file_paths = [os.path.join('data', f) for f in arcpy.ListRasters('*.tif')]