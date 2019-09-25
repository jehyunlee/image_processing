from ij import IJ
from ij.process import ImageStatistics as IS
import os

options = IS.MEAN | IS.MEDIAN | IS.MIN_MAX

def getStatistics(imp):
	""" Return statistics for the given ImagePlus """
	ip = imp.getProcessor()
	stats = IS.getStatistics(ip, options, imp.getCalibration())
	return stats.mean, stats.median, stats.min, stats.max

# Folder to read all images from:
folder = "//SynologyDrive//KIER_ArbeitPlatz//03_ImageJ_script_learning//A_Fiji_Scripting_Tutorial//images"

# Get statistics for each image in the folder
# whose file extension is '.tif':
path = os.getcwd()
path = path[:-8]
folder = path + folder

for filename in os.listdir(folder):
	if filename.endswith(".tif"):
		print("Processing", filename)
		fname = os.path.join(folder, filename)
		print(fname)
		imp = IJ.openImage(fname)
		if imp is None:
			print("Could not open image from file:", filename)
			continue
		mean, median, min, max = getStatistics(imp)
		print("Image statistics for ", imp.title)
		print("Mean: ", mean)
		print("Median: ", median)
		print("Min and Max: ", min, " - ", max)
	else:
		print("Ignoring", filename)
