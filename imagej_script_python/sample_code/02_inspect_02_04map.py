# looping
from ij import WindowManager as WM # WindowManager: ImageJ에 떠있는 창들을 관리.

# 방법 1: for looping
images = []
for id in WM.getIDList():
    images.append(WM.getImage(id))

# 방법 2: list comprehension
images = [WM.getImage(id) for id in WM.getIDList()]

# 방법 3: map operation
images = map(WM.getImage, WM.getIDList())

print("images=", images)