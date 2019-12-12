from script.imglib.math import Compute, Subtract, Multiply
from script.imglib.color import Red, Blue, RGBA
from script.imglib.algorithm import Gauss, Dither
from script.imglib import ImgLib
from ij import IJ

# Obtain a color image from the ImageJ samples
clown = ImgLib.wrap(IJ.openImage("https://imagej.nih.gov/ij/images/clown.jpg")) 

# Example 1: compose a new image manipulating the color channels of the clown image:
img = RGBA(Gauss(Red(clown), 10), 40, Multiply(255, Dither(Blue(clown)))).asImage()
print type(img)
ImgLib.wrap(img).show()