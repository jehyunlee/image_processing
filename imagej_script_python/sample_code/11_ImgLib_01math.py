from script.imglib.math import Compute, Subtract
from script.imglib.color import Red, Green, Blue, RGBA
from script.imglib import ImgLib
from ij import IJ 

# RGB image stack 열기
imp = IJ.openImage("https://imagej.nih.gov/ij/images/flybrain.zip")  

# Wrap it as an Imglib image
img = ImgLib.wrap(imp)

# Example 1: subtract red from green channel
sub = Compute.inFloats(Subtract(Green(img), Red(img)))
ImgLib.wrap(sub).show()

# Example 2: subtract red from green channel, and compose a new RGBA image  
rgb = RGBA(Red(img), Subtract(Green(img), Red(img)), Blue(img)).asImage()  
  
ImgLib.wrap(rgb).show()  