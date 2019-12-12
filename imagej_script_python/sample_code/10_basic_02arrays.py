from array import array, zeros
from ij import ImagePlus, IJ

# An empty native float array of length 5
a = zeros('f', 5)
print a

# A native float array with values 0 to 9
b = array('f', [0, 1, 2, 3, 4])
print b

# An empty native ImagePlus array of length 5
imps = zeros(ImagePlus, 5)
print imps

# Assign the current image to the first element of the array
imps[0] = IJ.getImage()
print imps

# Length of an array
print "length:", len(imps)
