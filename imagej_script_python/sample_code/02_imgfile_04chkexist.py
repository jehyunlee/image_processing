# 파일 이름 지정해서 저장
from ij import IJ
from ij.io import FileSaver
from os import path

imp = IJ.getImage()
fs = FileSaver(imp)

# image가 파일로 지정될 폴더
folder = "C://Arbeitplatz//03_ImageJ_script_learning//sample_code//images" 

# image 저장 폴더가 존재하는지 확인
if path.exists(folder) and path.isdir(folder):
    print "folder exists:", folder
    filepath = path.join(folder, "boats.tif") 
    if path.exists(filepath):
        print "File exists! Not saving the image, would overwrite a file!"
    elif fs.saveAsTiff(filepath)
        print "File save successfully at", filepath
else:
    print "Folder does not exist or it's not a folder!"
