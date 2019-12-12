# Load an image of the Drosophila larval fly brain and segment  
# the 5-micron diameter cells present in the red channel. 

from script.imglib.analysis import DoGPeaks
from script.imglib.color import Red 
from script.imglib.algorithm import Scale2D  
from script.imglib.math import Compute 
from script.imglib import ImgLib  
from ij3d import Image3DUniverse  
# from javax.vecmath import Color3f, Point3f  
from org.scijava.vecmath import Color3f, Point3f
from ij import IJ  

cell_diameter = 5    # in microns
minPeak = 40        # the minimum intensity for a peak to be considered so.
# imp = IJ.openImage("http://samples.fiji.sc//samples/first-instar-brain.zip")  
imp = IJ.openImage("http://samples.fiji.sc/first-instar-brain.zip") 

# Scale the X, Y axis down to isotropy with the Z axis
cal = imp.getCalibration()
width = cal.pixelWidth
depth = cal.pixelDepth
scale2D = width / depth
iso = Compute.inFloats(Scale2D(Red(ImgLib.wrap(imp)), scale2D))
print "width=%f, depth=%f" %(width, depth)
# ImgLib.wrap(iso).show()

# Find Peaks by difference of Gaussian
sigma = (cell_diameter / cal.pixelWidth) * scale2D
peaks = DoGPeaks(iso, sigma, sigma*0.5, minPeak, 1)
print "Found", len(peaks), "peaks"
# print peaks

# Convert the peaks into points in calibrated image space
ps = []
for peak in peaks:
    p = Point3f(peak) # peak의 (x, y, z) 좌표 추출
    p.scale(width * 1/scale2D)
    ps.append(p)

print ps 

# Show the peaks as spheres in 3D, along with orthoslices:
univ = Image3DUniverse(512, 512)
univ.addIcospheres(ps, Color3f(1, 0, 0), 2, cell_diameter/2, "Cells").setLocked(True)
univ.addOrthoslice(imp).setLocked(True)
univ.show()
