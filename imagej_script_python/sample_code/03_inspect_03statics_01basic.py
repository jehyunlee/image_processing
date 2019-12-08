# 이미지 통계 정보 추출
from ij import IJ
from ij.process import ImageStatistics as IS

# 떠 있는 이미지 캡처
imp = IJ.getImage()  # ImagePlus : title, dimension 등 이미지 정보를 포함.
  
# ImageProcessor 호출 
# ImageProcessor : ImagePlus 중 2D Image 부분 + 조작을 위한 기본 methods. ImageStack (3D 이상) 제외
# ImagePlus & ImageProcessor: https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html
ip = imp.getProcessor()  
  
options = IS.MEAN | IS.MEDIAN | IS.MIN_MAX  
# getStatistics: Calculates and returns uncalibrated (raw) statistics for the specified image, including histogram, area, mean, min and max, standard deviation and mode. 
# IS.getStatistics: https://imagej.nih.gov/ij/developer/api/ij/process/ImageStatistics.html#getStatistics-ij.process.ImageProcessor-int-ij.measure.Calibration-
stats = IS.getStatistics(ip, options, imp.getCalibration())
  
  
# 통계 데이터 출력  
print("Image statistics for", imp.title)
print("Mean:", stats.mean)  
print("Median:", stats.median)  
print("Min and max:", stats.min, "-", stats.max)  
            