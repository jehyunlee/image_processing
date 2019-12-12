import os
from ij import IJ, ImagePlus, VirtualStack
from mpicbg.ij.plugin import NormalizeLocalContrast
from loci.formats import ChannelSeparator

class FilterVirtualStack(VirtualStack):
    def __init__(self, width, height, sourceDir, params):
        # Tell the superclass to initialize itself with the sourceDir 
        super(VirtualStack, self).__init__(width, height, None, sourceDir)
        # Store the parameters for the NormalizeLocalContrast
        self.params = params
        # Set all TIFF files in sourceDir as slices
        for filename in sorted(os.listdir(sourceDir)):
            if filename.lower().endswith(".tif"):
                self.addSlice(filename)
    
    def getProcessor(self, n):
        # Load the image at index n
        filepath = os.path.join(self.getDirectory(), self.getFileName(n))
        imp = IJ.openImage(filepath)
        # Filter it:
        ip = imp.getProcessor()
        blockRadiusX = self.params["blockRadiusX"]
        blockRadiusY = self.params["blockRadiusY"]
        stds = self.params["stds"]
        center = self.params["center"]
        stretch = self.params["stretch"]
        NormalizeLocalContrast.run(ip, blockRadiusX, blockRadiusY, stds, center, stretch)
        return ip

# Parameters for the NormalizeLocalContrast plugin
params = {
    "blockRadiusX": 200,
    "blockRadiusY": 200,
    "stds": 2,
    "center": True,
    "stretch": True
}

# image size
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

def tiffImageFilenames(directory):  
    for filename in sorted(os.listdir(directory)):  
        if filename.lower().endswith(".tif"):  
            return filename         

sourceDir = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM"

first_path = os.path.join(sourceDir, tiffImageFilenames(sourceDir))  
print "first path=", first_path
width, height = dimensionsOf(first_path)
print "width, height=", width, height  

vstack = FilterVirtualStack(width, height, sourceDir, params)  

imp = ImagePlus("FilterVirtualStack with NormalizeLocalContrast", vstack)  
imp.show()  