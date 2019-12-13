from __future__ import with_statement 
from ij import IJ 
from ij.gui import PointRoi
from ij.measure import ResultsTable
from net.imglib2.img.display.imagej import ImageJFunctions as IL  
from net.imglib2.view import Views  
from net.imglib2.algorithm.dog import DogDetection
from jarray import zeros  

from operator import add
import csv, os

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
# imp.show()

# The minimum and maximum coordinates, for each image dimension,
# defining an interval within which pixel values will be summed.
minC = [-sigmaSmaller for i in xrange(img.numDimensions())]
maxC = [ sigmaSmaller for i in xrange(img.numDimensions())]


def centerAt(p, minC, maxC):
    """ Translate the minC, maxC coordinate bounds to the peak."""
    print "p, minC, maxC = ", p, minC, maxC
    pmin = map(add, p, minC)
    pmax = map(add, p, maxC)
    return pmin, pmax


def peakData(peaks, p, minC, maxC):
    """ A generator function that returns all peaks and their pixel sum, one at a time."""   
    for peak in peaks:
        peak.localize(p)
        minCoords, maxCoords = centerAt(p, minC, maxC)
        fov = Views.interval(img, minCoords, maxCoords)
        s = sum(t.getInteger() for t in fov)
        yield p, s

# Save as CSV file
folder = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\tmp"
fullpath = os.path.join(folder, 'peaks.csv')
with open(fullpath, 'wb') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar="\"", quoting=csv.QUOTE_NONNUMERIC)
    w.writerow(['x', 'y', 'sum'])
    for p, s in peakData(peaks, p, minC, maxC):
        w.writerow([p[0], p[1], s])

# Read the CSV file into an ROI
roi = PointRoi(0,0)
with open(fullpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header = reader.next() # advance reader by one line
    for x, y, s in reader:
        roi.addPoint(imp, float(x), float(y))

imp.show()
imp.setRoi(roi)
