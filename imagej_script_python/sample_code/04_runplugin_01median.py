from ij import IJ, ImagePlus
from ij.plugin.filter import RankFilters

imp = IJ.getImage()
ip = imp.getProcessor().convertToFloat()

# noise 제거를 위해서 media filter 적용
# radius = 2
radius = 2
# RankFilters class: mean, minimum, maximum, variance, outlier remval, despeckle 등이 구현됨.
# RankFilters(): 새로운 RankFilters instance 생성
#              .rank: RankFilters 내부 구현 method 호출. 
# https://javadoc.scijava.org/ImageJ1/ij/plugin/filter/RankFilters.html
RankFilters().rank(ip, radius, RankFilters.MEDIAN)

imp2 = ImagePlus(imp.title + "median_filtered", ip)
imp2.show()
