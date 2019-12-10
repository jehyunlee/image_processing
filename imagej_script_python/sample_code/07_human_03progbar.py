# progress bar

from ij import IJ

imp = IJ.getImage()
stack = imp.getImageStack()  

for i in xrange(1, stack.getSize()+1):
    # Report Progress
    IJ.showProgress(i, stack.getSize()+1)
    # 뭐라도 하기
    ip = stack.getProcessor(i)

# 완료
IJ.showProgress(1)    