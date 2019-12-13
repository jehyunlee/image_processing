from ij import IJ 
from ij.gui import PointRoi
from ij.measure import ResultsTable
from net.imglib2.img.display.imagej import ImageJFunctions as IL  
from net.imglib2.view import Views  
from net.imglib2.algorithm.dog import DogDetection
from jarray import zeros  

# Load a greyscale single-channel image: the "Embryos" sample image
imp = IJ.openImage("https://imagej.nih.gov/ij/images/embryos.jpg")
# imp.show()

# Convert it to 8-bit
IJ.run(imp, "8-bit", "")
# imp.show()

# Access its pixel data form an ImgLib2 data structure: a RandomAccessibleInterval  
img = IL.wrapReal(imp)

# View as an infinite image, mirrored at the endes which is ideal for Gaussians 
imgE = Views.extendMirrorSingle(img)

# Parameters for a Difference of Gaussian to detect embryo positions
calibration = [1.0 for i in range(img.numDimensions())]
print calibration   # [1.0, 1.0] : no calibration (identity)
sigmaSmaller = 15   # in pixels: a quarter of the radius of an embryo
sigmaLarger = 30    # in pixels: half the radius of an embryo
extremaType = DogDetection.ExtremaType.MAXIMA
minPeakValue = 10
normalizedMinPeakValue = False

# In the difference of gaussian peak detection, the img acts as the interval 
# within which to look for peaks. The Processing is done on the infinite imgE.
dog = DogDetection(imgE, img, calibration, sigmaSmaller, sigmaLarger, 
                   extremaType, minPeakValue, normalizedMinPeakValue)
peaks = dog.getPeaks()
print peaks                   

# Create a PointRoi from the DoG peaks, for visualization
roi = PointRoi(0, 0)
# A temporary array of integers, one per dimension the image has
p = zeros(img.numDimensions(), 'i')
print p
# Load every peak as a point in the PointRoi
for peak in peaks:  
    peak.localize(p)
    roi.addPoint(imp, p[0], p[1])

imp.setRoi(roi)
imp.show()

# Now, iterate each peak, defining a small interval centered at each peak,
# and measure the sum of total pixel intensity
# and display the results in an ImageJ ResultTable
table = ResultsTable()

for peak in peaks:
    # Read peak coordinates into an array of integers
    peak.localize(p)
    # Define limits of the interval around the peak:
    # (sigmaSmaller is half radius of the embryo)
    minC = [p[i] - sigmaSmaller for i in range(img.numDimensions())]
    maxC = [p[i] + sigmaSmaller for i in range(img.numDimensions())]
    print minC, maxC
    # View the interval around the peak, as a flat iterable (like an array)
    fov = Views.interval(img, minC, maxC)
    print fov
    # Compute sum of pixel intensity values of the interval
    # (the t is the Type that mediates access to the pixels, via its get* methods)
    s = sum(t.getInteger() for t in fov)
    # Add to results table
    table.incrementCounter()
    table.addValue("x", p[0])
    table.addValue("y", p[1])
    table.addValue("sum", s)

table.show("Embryo intensites at peaks")