# Flat-field correction: Flat-field correction is a technique used to improve quality in digital imaging. The goal is to remove artifacts from 2-D images that are caused by variations in the pixel-to-pixel sensitivity of the detector and/or by distortions in the optical path. It is a standard calibration procedure in everything from pocket digital cameras to giant telescopes.
# very large radius의 median을 실행해서 flat-field image를 simulation할 수 있으나, computing cost가 높아 대신 scale down된 image에 Gauss를 적용하고 원본 이미지만큼 scale up.
# 결과물 이상함. 추후 코드 확인 및 수정

from script.imglib.math import Compute, Divide, Multiply, Subtract
from script.imglib.algorithm import Gauss, Scale2D, Resample
from script.imglib import ImgLib 
from ij import IJ

# 1. Open an image
img = ImgLib.wrap(IJ.openImage("https://imagej.nih.gov/ij/images/bridge.gif"))
ImgLib.wrap(img).show()  

# 2. Simulate a bright field from a Gauss with a large radius
# (First scale down by 4x, then gauss of radius=20, then scale up)
brightfield = Resample(Gauss(Scale2D(img, 0.25), 20), img.getDimensions()) 
_bf = Compute.inFloats(brightfield)
ImgLib.wrap(_bf).show() # 회색으로 보이지만 ImageJ가 range를 -3.4e3 ~ 3.4e38로 인식해서 발생하는 문제임.

# 3. Simulate a perfect darkfield
darkfield = 0

# 4. Compute the mean pixel intensity value of the image
mean = reduce(lambda s, t: s + t.get(), img, 0) / img.size()  

# 5. Correct the illumination
corrected = Compute.inFloats(Multiply(Divide(Subtract(img, brightfield),  
                                             Subtract(brightfield, darkfield)), mean))  

ImgLib.wrap(corrected).show()  
