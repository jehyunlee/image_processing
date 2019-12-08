#filter
from ij import WindowManager as WM

# 떠 있는 모든 창 list
imps = map(WM.getImage, WM.getIDList())

def match(imp):
    """ Returns true if the name title contains the given word"""
    return imp.title.find("boats") > -1

# Method 1: 'for' loop
# 별도의 리스트를 생성해야 함.
matching = []
for imp in imps:
    if match(imp):
        matching.append(imp)

# Method 2: list comprehension
matching = [imp for imp in imps if match(imp)]

# method 3: 'filter' operation
# filter 명령을 사용하면 코드가 매우 짧아진다.
matching = filter(match, imps)

print(matching)
