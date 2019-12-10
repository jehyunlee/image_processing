# 밑바닥부터 이미지 만들기
from ij import ImagePlus
from ij.process import FloatProcessor
from array import zeros
from random import random

width = 1024
height = 1024
# Jython으로 array 만들기
# http://fiji.sc/wiki/index.php/Jython_Scripting_Examples#Creating_multi-dimensional_native_java_arrays
pixels = zeros('f', width * height) # f: "float"

for i in xrange(len(pixels)):
    pixels[i] = random()
    
fp = FloatProcessor(width, height, pixels, None)
imp = ImagePlus("White noise", fp)

imp.show()
