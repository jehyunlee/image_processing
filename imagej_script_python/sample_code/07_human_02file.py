# 파일 선택하는 창 띄우기
from ij.io import OpenDialog

od = OpenDialog("Choose a file", None)
filename = od.getFileName()

if filename is None:
    print "User cancelled the dialog!"
else:
    directory = od.getDirectory()
    filepath = directory + filename
    print "Selected file path:", filepath
    