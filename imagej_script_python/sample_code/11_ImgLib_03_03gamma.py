# Correct gamma
from script.imglib.math import Min, Max, Exp, Multiply, Divide, Log
from script.imglib.color import RGBA, Red, Green, Blue
from ij import IJ
from script.imglib import ImgLib 

gamma = 0.5
# img = ImgLib.wrap(IJ.getImage())
img = ImgLib.wrap(IJ.openImage("https://imagej.nih.gov/ij/images/clown.jpg"))  
ImgLib.wrap(img).show()

def g(channel, gamma):
    """ Return a function that, when evaluated, computes the gamma 
        of the given color channel. 
        If 'i' was the pixel value, then this function would do: 
        double v = Math.exp(Math.log(i/255.0) * gamma) * 255.0); 
        if (v < 0) v = 0; 
        if (v >255) v = 255; 
    """  
    return Min(255, Max(0, Multiply(Exp(Multiply(gamma, Log(Divide(channel, 255)))), 255)))  

corrected = RGBA(g(Red(img), gamma), g(Green(img), gamma), g(Blue(img), gamma)).asImage() 

ImgLib.wrap(corrected).show()
