# 이미지 전체에서 최소픽셀값 빼기
from ij import IJ, ImagePlus  
from ij.process import FloatProcessor  
  
imp = IJ.getImage()  
ip = imp.getProcessor().convertToFloat() # as a copy  
pixels = ip.getPixels()  

# Built-in 함수 사용 (min, reduce)  
# pixels를 훑으며 min 적용
minimum = reduce(min, pixels)  
  
# Method 1: for loop을 적용해서 모든 pixel 값을 직접 변경 
for i in xrange(len(pixels)):  
  pixels[i] -= minimum  
# 변경된 pixel값들로 새 이미지 만들기:  
imp2 = ImagePlus(imp.title, ip)  
  
# Method 2: 모든 pixel에서 최소값을 뺀 결과를 다른 배열(pixel3)에 저장  
pixels3 = map(lambda x: x - minimum, pixels)  
# 배열로부터 이미지 만들기  
ip3 = FloatProcessor(ip.width, ip.height, pixels3, None) # None: color  
imp3 = ImagePlus(imp.title, ip3)  
  
# Show the images in an ImageWindow:  
imp2.show()  
imp3.show()  