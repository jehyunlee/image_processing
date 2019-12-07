# threshold 이상 pixel 갯수 세기
from ij import IJ

imp = IJ.getImage()
ip = imp.getProcessor().convertToFloat()
pixels = ip.getPixels()

# 평균값 계산: 총합을 pixel 수로 나누기
mean = sum(pixels)/len(pixels)

# 평균 이상 pixel 수 세기
n_pix_above = reduce(lambda count, a: count + 1 if a > mean else count, pixels, 0)

print("Mean value:", mean)
print("{} pixels above mean".format(n_pix_above/float(len(pixels)) *!00))
