from ij import IJ
from ij.process import ImageStatistics as IS

# Grab the active image
imp = IJ.getImage()

# Get its ImageProcessor
ip = imp.getProcessor()

options = IS.MEAN | IS.MEDIAN | IS.MIN_MAX
stats = IS.getStatistics(ip, options, imp.getCalibration())

# print statistics on the image
print("Image statistics for", imp.title)
print("Mean: ", stats.mean)
print("Median: ", stats.median)
print("Min and Max: ", stats.min, " - ", stats.max)
