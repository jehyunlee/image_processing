# 폴더 선택하는 창 띄우기
from ij.io import DirectoryChooser

dc = DirectoryChooser("Choose a folder")
folder = dc.getDirectory()

if folder is None:
    print "User cancelled the dialog!"
else:
    print "Selected folder:", folder
    