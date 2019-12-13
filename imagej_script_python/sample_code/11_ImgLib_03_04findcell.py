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
# Perform a difference of Gaussian on the given Image, and this class itself becomes the List of found peaks, each as a float[] array that specifies its position
# https://javadoc.scijava.org/Fiji/script/imglib/analysis/DoGPeaks.html
# https://javadoc.scijava.org/Fiji/mpicbg/imglib/algorithm/scalespace/DifferenceOfGaussian.html
# Extracts local minima and maxima of a certain size. It therefore computes the difference of gaussian for an Image and detects all local minima and maxima in 3x3x3x....3 environment, which is returned as an ArrayList of DifferenceOfGaussianPeaks. The two sigmas define the scale on which extrema are identified, it correlates with the size of the object. Note that not only extrema of this size are found, but they will have the higher absolute values. Note as well that the values of the difference of gaussian image is also defined by the distance between the two sigmas. A normalization if necessary can be found in the ScaleSpace class. Also note a technical detail, the method findPeaks(Image img) can be called on any image if the image from where the extrema should be computed already exists.
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
# Image3DUniverse(int width, int height): Constructs a new universe with the specified width and height.
univ = Image3DUniverse(512, 512)
# addIcospheres(List<Point3f> points, Color3f color, int subdivisions, float radius, String name)
univ.addIcospheres(ps, Color3f(1, 0, 0), 2, cell_diameter/2, "Cells").setLocked(True)
univ.addOrthoslice(imp).setLocked(True)
univ.show()
