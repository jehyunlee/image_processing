# VirtualStack의 slice를 하드에 저장
import os, sys
from ij import IJ, ImagePlus, VirtualStack
from loci.formats import ChannelSeparator

sourceDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM"
targetDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\output"

# Read the dimensions of the image at path by parsing the file header only,  
# thanks to the LOCI Bioformats library  
def dimensionsOf(path):
    fr = None
    try:
        fr = ChannelSeparator()
        fr.setGroupFiles(False)
        fr.setId(path)
        return fr.getSizeX(), fr.getSizeY()
    except:
        # 에러가 있다면 출력
        print sys.exc_info()
    finally:
        fr.close()

# A generator over all file paths in sourceDir
def tiffImageFilenames(directory):  
    for filename in sorted(os.listdir(directory)):  
        if filename.lower().endswith(".tif"):  
            yield filename  

# Read the dimensions from the first image  
first_path = os.path.join(sourceDir, tiffImageFilenames(sourceDir).next())  
width, height = dimensionsOf(first_path)  

# Create the VirtualStack without a specific ColorModel  
# (which will be set much later upon loading any slice)  
vstack = VirtualStack(width, height, None, sourceDir)  

# Add all TIFF images in sourceDir as slices in vstack  
for filename in tiffImageFilenames(sourceDir):  
    vstack.addSlice(filename)  
  
# Visualize the VirtualStack  
imp = ImagePlus("virtual stack of images in " + os.path.basename(sourceDir), vstack)  
# imp.show()  

from mpicbg.ij.plugin import NormalizeLocalContrast
from ij.io import FileSaver

# slice마다 process 후 targetDir에 save
for i in xrange(0, vstack.size()):
    ip = vstack.getProcessor(i+1)   # slice list는 1부터 시작 (1-based listing)
    # NormalizeLocalContrast plugin을 ImageProcessor에 적용
    NormalizeLocalContrast.run(ip, 200, 200, 3, True, True)
    # 결과 저장
    name = vstack.getFileName(i+1)
    if not name.lower().endswith(".tif"):
        name += ".tif"
    FileSaver(ImagePlus(name, ip)).saveAsTiff(os.path.join(targetDir, name))
