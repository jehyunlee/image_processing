# pixel value로 filtering
from ij import IJ

imp = IJ.getImage()
ip = imp.getProcessor().convertToFloat()
pixels = ip.getPixels()

# 평균값 계산
mean = sum(pixels)/len(pixels)

# 평균값 이상 pixel의 index를 list로 저장
above = filter(lambda i: pixels[i] > mean, xrange(len(pixels)))
print "Number of pixels above mean value:", len(above)

# 평균값 이상 pixel들의 center of mass 계산

# image width : pixel의 위치 파악에 활용.
width = imp.width

# Method 1: for loop
xc = 0
yc = 0
for i in above:
    xc += i % width # index i pixel의 x 좌표
    yc += i // width # index i pixel의 y 좌표
xc = xc/len(above)
yc = yc/len(above)
print xc, yc

# Method 2: sum과 map 사용
xc = sum(map(lambda i: i%width, above)) / len(above)
yc = sum(map(lambda i: i/width, above)) / len(above)
print xc, yc

# Method 3: list "above"를 단 한번만 iterate
xc, yc = [d/len(above) for d in reduce(lambda c, i: [c[0] + i % width, c[1] + i / width], above, [0, 0])] 
print xc, yc

# Method 4: list "above"를 단 한번만 iterate하지만 더 깔끔하고 성능 좋게
from functools import partial

def accum(width, c, i):
    """ index가 i인 X, Y 좌표들을 list c로 수집 """
    c[0] += i % width
    c[1] += i / width
    return c

xc, yc = [d/len(above) for d in reduce(partial(accum, width), above, [0, 0])]
print xc, yc
