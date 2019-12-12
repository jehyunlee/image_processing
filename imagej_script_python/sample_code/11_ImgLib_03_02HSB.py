from script.imglib.math import Compute, Add, Subtract
from script.imglib.color import HSB, Hue, Saturation, Brightness
from script.imglib import ImgLib
from ij import IJ

# Obtain an image
img = ImgLib.wrap(IJ.openImage("https://imagej.nih.gov/ij/images/clown.jpg"))  

# Obtain a new clown, whose hue has been shifted by half  
# with the same saturation and brightness of the original
bluey = Compute.inRGBA(HSB(Add(Hue(img), 0.5), Saturation(img), Brightness(img)))

print type(Hue(img)), type(Saturation(img)), type(Brightness(img))

ImgLib.wrap(Compute.inFloats(Hue(img))).show()
ImgLib.wrap(Compute.inFloats(Saturation(img))).show()
ImgLib.wrap(Compute.inFloats(Brightness(img))).show()


ImgLib.wrap(bluey).show()
