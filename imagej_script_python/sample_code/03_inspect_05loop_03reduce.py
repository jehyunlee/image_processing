# reduce
from ij import IJ
from ij import WindowManager as WM

# 열린 이미지 list
imps = map(WM.getImage, WM.getIDList())

def area(imp):
    return imp.width * imp.height
    

# Method 1: 'for' loop
largest = None
largestArea = 0
for imp in imps:
    a = area(imp)
    if largest is None:
        largest = imp
        largestArea = a
    else:
        if a > largestArea:
            largest = imp
            largestArea = a           

# Method 2: 'reduce'
def largestImage(imp1, imp2):
    return imp1 if area(imp1) > area(imp2) else imp2

largest = reduce(largestImage, imps)

print "Largest image=", largest.title
print "Largest area=", largestArea 
