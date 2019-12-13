# Views: https://javadoc.scijava.org/ImgLib2/net/imglib2/view/Views.html

from ij import IJ 
from net.imglib2.img.display.imagej import ImageJFunctions as IL  
from net.imglib2.view import Views
# ImgLib2 : dimension-independent, data source-independent, image type-independent

imp = IJ.openImage("https://imagej.nih.gov/ij/images/clown.jpg")
# imp.show()

# Convert to 8-bit if it isn't yet, using macros
IJ.run(imp, "8-bit", "")
# imp.show()

# Access its pixel data from an ImgLib2 RandomAccessibleInterval
img = IL.wrapReal(imp)

# View as an infinite image, with a value of zero beyond the image edges
# extendZero(F source): Extend a RandomAccessibleInterval with a constant-value out-of-bounds strategy where the constant value is the zero-element of the data type.
# imgE = Views.extendZero(img)

# View mirroring the data beyond the edges  
imgE = Views.extendMirrorSingle(img)  

# Limit the infinite image with an interval twice as large as the original,
# so that the original image remains at the center.
# It starts at minus half the image width, and ends at 1.5x the image width.
minC = [int(-0.5 * img.dimension(i)) for i in range(img.numDimensions())]
maxC = [int( 1.5 * img.dimension(i)) for i in range(img.numDimensions())]
print img.dimension(0), img.dimension(1)
print minC, maxC
# interval(RandomAccessible randomAccessible, long[] min, long[] max): Define an interval on a RandomAccessible. It is the callers responsibility to ensure that the source RandomAccessible is defined in the specified interval.
imgL = Views.interval(imgE, minC, maxC)

# Visualize the enlarged canvas, so to speak  
imp2 = IL.wrap(imgL, imp.getTitle() + " - enlarged canvas") # an ImagePlus  
imp2.show()

