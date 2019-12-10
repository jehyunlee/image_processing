# dimensionsOf : image file의 heaer를 읽어서 width, height를 추출

import os, sys
from ij import IJ, ImagePlus, VirtualStack
from loci.formats import ChannelSeparator

sourceDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM"

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
        # 에러 발생시 출력
        print sys_exc_info()
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
imp.show()  