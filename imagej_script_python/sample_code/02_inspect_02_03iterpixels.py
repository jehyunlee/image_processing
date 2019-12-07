# pixel 단위 정보 추출
from ij import IJ 
from sys.float_info import max as MAX_FLOAT

# 떠 있는 이미지 캡처
imp = IJ.getImage()

# ImageProcessor에 담긴 정보를 float로 변환
ip = imp.getProcessor().convertToFloat()
# pixel 정보
pixels = ip.getPixels()

print("Image is", imp.title, "of type", imp.type)

# pixel 최소값 구하기

# 방법 1. C언어 스타일의 for loop
minimum = MAX_FLOAT
for i in xrange(len(pixels)):
    if pixels[i] < minimum:
        minimum = pixels[i]
 
print("1. Minimum is:", minimum)

# 방법 2. pixel을 list 형태로 iterate
minimum = MAX_FLOAT
for pix in pixels:
    if pix < minimum:
        minimum = pix

print("2. Minimum is:", minimum)

# 방법 3. 내장(built-in)함수 사용
minimum = reduce(min, pixels)

print("3. Minimum is:", minimum)
