from ij import IJ
from ij.io import FileSaver
from os import path

imp = IJ.getImage()
fs = FileSaver(imp)

folder = "C://Users//sec//SyNologyDrive//KIER_ArbeitPlatz//03_ImageJ_script_learning//A_Fiji_Scripting_Tutorial//images"

if path.exists(folder) and path.isdir(folder):
	print("foler exists: ", folder)
	filepath = path.join(folder, "boats.tif") 
	if path.exists(filepath):
		print("File exists! Not saving the image, would overwrite a file!")
		
	elif fs.saveAsTiff(filepath):
		print("File saved successfully at", filepath)

else:
	print("folder does not exist or it's not a folder!")
