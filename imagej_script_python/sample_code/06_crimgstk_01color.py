# color image stack을 불러와서 green channel 추출
from ij import IJ, ImagePlus, ImageStack

# fly brain image (RGB)
imp = IJ.openImage("https://imagej.nih.gov/ij/images/flybrain.zip")
imp.show()
stack = imp.getImageStack()

print "number of slices:", imp.getNSlices()

# green slice list
greens = []

# stack 전체에 green slide를 iterate
for i in xrange(1, imp.getNSlices()+1):
    # index i의 ColorProcessor를 추출
    cp = stack.getProcessor(i)
    # green channel을 FloatProcessor로 추출
    fp = cp.toFloat(1, None) # R: 0, G: 1, B: 2
    # 리스트로 저장
    greens.append(fp)
    
# green channel만 있는 stack 생성
stack2 = ImageStack(imp.width, imp.height)
for fp in greens:
        # 'ip'에 들어있는 image를 'sliceLabel'과 함께 맨 뒤 slice로 추가.
        stack2.addSlice(None, fp) # addSlice(java.lang.String sliceLabel, ImageProcessor ip)

# green channel stack으로 새 이미지 생성
imp2 = ImagePlus("Green channel", stack2)
# green look-up table 설정
IJ.run(imp2, "Green", "")
imp2.show()