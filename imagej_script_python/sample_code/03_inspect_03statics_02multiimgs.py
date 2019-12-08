# 이미지 통계 정보 일괄 추출
from ij import IJ  
from ij.process import ImageStatistics as IS  
import os  
  
options = IS.MEAN | IS.MEDIAN | IS.MIN_MAX  

# 이미지를 넣으면 평균, 중간값, 최소, 최대를 추출하는 함수  
def getStatistics(imp):  
  """ Return statistics for the given ImagePlus """  
  ip = imp.getProcessor()  
  stats = IS.getStatistics(ip, options, imp.getCalibration())  
  return stats.mean, stats.median, stats.min, stats.max  
  
  
# 이미지를 읽어올 폴더:  
# Error: folder = r"C://Arbeitplatz//03_ImageJ_script_learning//sample_code//images//SEM"
# Error: folder = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM"
folder = r"C:\Arbeitplatz\03_ImageJ_script_learning\sample_code\images\SEM" # unicode 문자열을 raw 문자열로 바꿔주기
  
# 확장자가 ".tif"인 파일들로부터 데이터 읽어오기.
for filename in os.listdir(folder):  
  if filename.endswith(".tif"):  
    print("Processing", filename)
    fullpath = os.path.join(folder, filename)
    print("fullpath", fullpath)  
    imp = IJ.openImage(fullpath)  
    if imp is None:  
      print("Could not open image from file:", filename)  
      continue  
    mean, median, min, max = getStatistics(imp)  
    print("Image statistics for", imp.title)  
    print("Mean:", mean)  
    print("Median:", median)  
    print("Min and max:", min, "-", max)  
  else:  
    print("Ignoring", filename)