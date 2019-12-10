# 이미지 기본 정보 추출
from ij import IJ, ImagePlus

# 떠 있는 이미지 캡처
imp = IJ.getImage()

# 이미지 정보 추출
print "title:", imp.title
print "width:", imp.width
print "height:", imp.height  
print "number of pixels:", imp.width * imp.height  
print "number of slices:", imp.getNSlices()  
print "number of channels:", imp.getNChannels()  
print "number of time frames:", imp.getNFrames()  
  
types = {ImagePlus.COLOR_RGB : "RGB",  
         ImagePlus.GRAY8 : "8-bit",  
         ImagePlus.GRAY16 : "16-bit",  
         ImagePlus.GRAY32 : "32-bit",  
         ImagePlus.COLOR_256 : "8-bit color"}  
  
print "image type:", types[imp.type]