# RGB stack을 두 개로 분리된 hyperstack으로 변환.
# 각 stack은 32-bit FloatProcessor.
from ij import IJ, ImagePlus, ImageStack, CompositeImage

# fly brain image (RGB)
imp = IJ.openImage("https://imagej.nih.gov/ij/images/flybrain.zip")
stack = imp.getImageStack()

# hyperstack data를 저장할 새로운 stack
stack2 = ImageStack(imp.width, imp.height)

# stack의 각 color slice를 두 개의 32-bit FloatProcessor slice로 변환
for i in xrange(1, imp.getNSlices()+1):
    # index i의 ColorProcessor 추출
    cp = stack.getProcessor(i)
    # Red, Green channel을 FloatProcessor로 추출
    red = cp.toFloat(0, None)
    green = cp.toFloat(1, None)
    # red와 green을 stack2에 추가
    stack2.addSlice(None, red)
    stack2.addSlice(None, green)

# stack2로 ImagePlus 생성
imp2 = ImagePlus("32-bit 2-channel composite", stack2)
# imp의 spatial and density calibraion data를 가져와 적용
imp2.setCalibration(imp.getCalibration().copy()) # https://imagej.nih.gov/ij/developer/api/ij/measure/Calibration.html

# stack2의 slice를 hyperstack form으로 표현하고 CompositeImage로 open.
nChannels = 2              # two color channels
nSlices = stack.getSize()  # original image의 stack 수
nFrames = 1                # one time point만
imp2.setDimensions(nChannels, nSlices, nFrames)
comp = CompositeImage(imp2, CompositeImage.COLOR)
comp.show()
