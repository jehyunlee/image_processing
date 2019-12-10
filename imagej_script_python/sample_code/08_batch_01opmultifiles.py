# 다수 함수에 동일 operation 적용
# Local Contrast Normalization : https://josvandewolfshaarblog.wordpress.com/2016/02/06/local-contrast-normalization-in-theano/
import os, sys
from mpicbg.ij.plugin import NormalizeLocalContrast
from ij import IJ, ImagePlus
from ij.io import FileSaver

sourceDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM"
targetDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\output"

# input image를 받아서 contrast-normalize하는 함수
def normalizeContrast(imp):
    # slide box 크기
    blockRadiusX = 200 # pixel 단위
    blockRadiusY = 200
    # The number of standard deviations to expand to  
    stds = 2
    # Whether to expand from the median value of the box or the pixel's value
    center = True
    # Whether to stretch the expanded values to the pixel depth of the image  
    # e.g. between 0 and 255 for 8-bit images, or e.g. between 0 and 65536, etc.  
    stretch = True
    
    # Duplicate the ImageProcessor
    copy_ip = imp.getProcessor().duplicate()
    # Contrast Normalization을 copy에 적용
    NormalizeLocalContrast().run(copy_ip,  blockRadiusX, blockRadiusY, stds, center, stretch)
    # Return as new image
    return ImagePlus(imp.getTitle(), copy_ip)

# File path를 입력받아서 image로 읽고, normalize하고, 다른 디렉토리에 저장하는 함수
def loadProcessAndSave(sourcepath, fn):
    try:
        imp = IJ.openImage(sourcepath)
        norm_imp = fn(imp) # 함수 fn을 실행. 여기서는 'normalizeContrast'
        targetpath = os.path.join(targetDir, os.path.basename(sourcepath))
        if not targetpath.endswith(".tif"):
            targetpath += ".tif"
        FileSaver(norm_imp).saveAsTiff(targetpath)
    except:
        print "Could not load or process file:", sourcepath
        print sys.exc_info()

# Strategy #1: nested directories with os.listdir and os.path.isdir
def processDirectory(theDir, fn):
    """ For every file in theDir, check if it is a directory, if so, invoke recursively. 
        If not a directory, invoke 'loadProcessAndSave' on it. """ 
    for filename in  os.listdir(theDir):
        path = os.path.join(theDir, filename)
        if os.path.isdir(path):
            # Recursive call
            processDirectory(path, fn)
        else:
            loadProcessAndSave(path, fn)

# Launch strategy 1:
# processDirectory(sourceDir, normalizeContrast)

# Strategy #2: os.walk에게 맡김
for root, directories, filenames in os.walk(sourceDir):
    for filename in filenames:
        loadProcessAndSave(os.path.join(root, filename), normalizeContrast)
