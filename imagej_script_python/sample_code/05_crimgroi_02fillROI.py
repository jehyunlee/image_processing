# 선택 영역 칠하기
from ij import ImagePlus
from ij.process import FloatProcessor
from array import zeros
from random import random
from ij.gui import Roi, PolygonRoi

# noise로 칠해진 이미지 생성
width = 1024
height = 1024
pixels = zeros('f', width * height)

for i in xrange(len(pixels)):
    pixels[i] = random()
    
fp = FloatProcessor(width, height, pixels, None)
imp = ImagePlus("Random", fp)

imp.show()

# 직사각형 관심영역(ROI: Region of Interest)를 2로 채우기
fp = FloatProcessor(width, height, pixels, None)
roi = Roi(400, 200, 400, 300) # Roi(int x, int y, int width, int height)
fp.setRoi(roi)
fp.setValue(2.0)
fp.fill()

imp2 = ImagePlus("Rectangle", fp) 
imp2.show()

# Polygon ROI를 -3으로 채우기
fp = FloatProcessor(width, height, pixels, None)
xs = [234, 174, 162, 102, 120, 123, 153, 177, 171,  
      60, 0, 18, 63, 132, 84, 129, 69, 174, 150,  
      183, 207, 198, 303, 231, 258, 234, 276, 327,  
      378, 312, 228, 225, 246, 282, 261, 252]  
ys = [48, 0, 60, 18, 78, 156, 201, 213, 270, 279,  
      336, 405, 345, 348, 483, 615, 654, 639, 495,  
      444, 480, 648, 651, 609, 456, 327, 330, 432,  
      408, 273, 273, 204, 189, 126, 57, 6]  
proi = PolygonRoi(xs, ys, len(xs), Roi.POLYGON) # PolygonRoi(float[] xPoints, float[] yPoints, int nPoints, int type) 
fpp = fp
fpp.setRoi(proi)
fpp.setValue(-3)
fpp.fill(proi.getMask())      

imp3 = ImagePlus("Polygon", fpp) 
imp3.show()