# 화면에 떠있는 그림 저장

from ij import IJ

imp = IJ.getImage()
print imp

from ij.io import FileSaver
fs = FileSaver(imp)
fs.save()
