# Virtual Stack: individual slice를 메모리에 저장하는 대신 slice를 생성하는 recipe를 저장
from ij import IJ, ImagePlus, VirtualStack

imp = IJ.getImage()
roi = imp.getRoi()
stack = imp.getStack()

class CroppedStack(VirtualStack):
    def __init__(self):
        # Constructor: tell the superclass VirtualStack about the dimensions  
        super(VirtualStack, self).__init__(stack.getWidth(), stack.getHeight(), stack.size())
    
    def getProcessor(self, n):
        # Modify the same slice at index n every time it is requred
        ip = stack.getProcessor(n)
        ip.setRoi(roi)
        return ip.crop()

cropped = ImagePlus("cropped", CroppedStack())
cropped.show()
