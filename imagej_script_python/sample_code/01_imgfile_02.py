# 파일 이름 지정해서 저장
from ij import IJ
from ij.io import FileSaver

imp = IJ.getImage()
fs = FileSaver(imp)

# image가 파일로 지정될 폴더
folder = "C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images"

filepath = folder + "\" + "boats.tif"
print(filepath)
fs.saveAsTiff(filepath)