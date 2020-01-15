---
title: 6. Image Data 추출
categories:
  - ImageJ
  - Tutorial
comments: false
thumbnail: /thumbnails/ImageJ-Tutorial/6_insp_1.PNG
date: 2019-12-19 12:00:00
---
### 6.1. `ImagePlus`: `ImageJ`의 이미지 `instance`

**Reference**

> [TCP School 26) 클래스의 개념](http://tcpschool.com/java/java_class_intro)
> [ImagePlus](https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html)

* [지난 글](https://jehyunlee.github.io/2019/12/19/ImageJ-tutorial-5-Script/)에서 객체지향 프로그래밍(OOP: Object Oriented Programming)의 개념을 짧게 설명했습니다.
* `instance`란 것은 `Class`에 정의된 대로 만들어진 객체입니다. 
  * 자동차 설계도(`Class`)와 자동차(`instance`) 관계로 보시면 비슷합니다.
  * `instance`는 `Class`에 선언된 `Field`와 `Method`를 가지고 있습니다.
    (ex. 그랜저 `Class`로 만들어진 철수 차 `instance`의  후방카메라 옵션)
  * 다른 `Class`로 만든 `instance`끼리는 당연히 다르고 (ex. 람보르기니 vs 그랜저)
  * 같은 `Class`로 만든 `instance`라도 다른 존재입니다 (ex. 철수 차 vs 영희 차)
* `ImageJ`에서 이미지를 읽어들이면 [`ImagePlus`](https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html) instance가 됩니다.
  * [공식 문서](https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html)를 클릭해보시면 자체적으로 `changes`부터 `win`까지, 그리고 상위 클래스인 `java.awt.image.ImageObserver`와 `ij.measure.Measurements`로부터 상속받은 `Field`가 추가로 상당히 많습니다.
  * 그랜저 `Class`는 자동차 `Class`에 포함되므로 내연기관, 바퀴, 헤드라이트 등 자동차의 속성을 물려받습니다. 이 것을 `상속(inheritance)`이라고 합니다.

### 6.2. 이미지 정보 추출

**Reference**

> [A Fiji Scripting Tutorial #3. Inspecting properties and pixels of an image](https://www.ini.uzh.ch/~acardona/fiji-tutorial/#s3) 
> [ImageStatistics](https://javadoc.scijava.org/ImageJ1/ij/process/ImageStatistics.html)
> [ImageProcessor](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html)

* `ImageJ`에서 이미지를 읽으면 `ImagePlus`형식으로 받아들인다고 했고, `ImagePlus`는 여러 정보(`Field`)를 담고 있다고 했습니다. 
* 그럼 이 정보를 어떻게 꺼내볼까요?
* `Class` `instance`의 `Field`에 접근할 때는 `[Instance이름].[Field이름]`으로 접근합니다. 
  * 철수가 그랜저 (Class: `Grandeur`)를 새로 샀다고 합시다.
  * 철수네 자동차 (Instance: `CScar`)의 색상(Field: `color`)은 `CScar.color` 입니다.
  * 철수네 자동차 색상을 출력하라고 하려면, `print CScar.color`라고 하면 됩니다.



#### 6.2.1. 이미지 기본 정보 추출

* [`이미지 파일 구조`](https://jehyunlee.github.io/2019/12/16/ImageJ-tutorial-2-ImageFileStructure/) 글에서, 이미지는 x, y 2차원 공간에 놓인 픽셀들로 구성되며 이미지 파일에는 `Channels`, `Slices`, `Frames` 속성이 있다고 말씀드렸습니다.

* 이 데이터들을 뽑아보겠습니다.

* `File > Open Samples > Boats.gif`로 배 이미지를 엽니다.

* 단축키 `[`를 눌러 아래 코드를 붙여넣고 실행합니다. [여기에서 다운로드](https://github.com/jehyunlee/image_processing/blob/master/imagej_script_python/sample_code/03_inspect_01imageplus.py)도 가능합니다.
  ```python
  # 이미지 기본 정보 추출
  from ij import IJ, ImagePlus
  
  # 떠 있는 이미지 캡처
  imp = IJ.getImage()
  
  # 이미지 정보 추출
  print "title:", imp.title
  print "width:", imp.width
  print "height:", imp.height  
  print "number of pixels:", imp.width * imp.height  
  print "number of slices:", imp.getNSlices()  
  print "number of channels:", imp.getNChannels()  
  print "number of time frames:", imp.getNFrames()  
  
  types = {ImagePlus.COLOR_RGB : "RGB",  
           ImagePlus.GRAY8 : "8-bit",  
           ImagePlus.GRAY16 : "16-bit",  
           ImagePlus.GRAY32 : "32-bit",  
           ImagePlus.COLOR_256 : "8-bit color"}  
  
  print "image type:", types[imp.type]
  ```
* 위 코드를 실행하면 아래와 같이 출력됩니다.

  ```python
  # 실행결과
  title: boats.gif
  width: 720
  height: 576
  number of pixels: 414720
  number of slices: 1
  number of channels: 1
  number of time frames: 1
  image type: 8-bit
  ```
  
  ![ ](6_insp_1.PNG)
  * 코드 맨 마지막 부분, `print "image type:", types[imp.type]` 의 결과물로 `image type: 8-bit`이 출력되었습니다.  
  * 읽어들인`boats.gif`의 type이 `ImagePlus`의  `GRAY8`형식이기 때문에 `imp.type`은 `ImagePlus.GRAY8`로 치환되었고, `python`의 데이터 타입 중 하나인 `dictionary` 호출에 따라 `types`에서 `ImagePlus.GRAY8`에 해당하는 값인 `8-bit`가 출력된 것입니다.
  
* `image type`은 이 이미지의 픽셀이 어떻게 구성되어 있는지를 보여줍니다.

  * GRAY8 : 흑백. 한 `pixel`은 8 bit ($ 2^8 = 256 $개)의 정수값(0~255)을 가질 수 있습니다. 
  * GRAY16 : 흑백. 한 `pixel`은 8 bit ($ 2^16 = 65536 $개)의 정수값(0~65535)을 가질 수 있습니다.
  * GRAY32 : 흑백. 한 `pixel`은 32 bit의 소수(`float`)값을 가질 수 있습니다.
  * COLOR_256: 컬러. 한 `pixel`은 3 개(Red, Green, Blue)의 8 bit 채널을 가집니다.
  * COLOR_RGB: 컬러. 한 `pixel`은 3 개(Red, Green, Blue)의 32 bit 채널을 가집니다.

<br>

#### 6.2.2. 이미지 통계 정보 추출

* 위에서 `boats.gif`는 720 x 576 = 414,720개의 `pixel`로 이루어져 있음을 알 수 있습니다.
* 이미지는 상당히 많은 수의 `pixel`로 이루어져 있기 때문에 전체적인 통계 데이터를 파악할 필요가 있습니다.
* `ImageJ`는 이미지 통계 분석을 위해 [`ImageStatistics`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageStatistics.html)라는 모듈을 제공합니다.
  * `ImageStatistics` 가 입력으로 [`ImageProcessor`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html)를 읽어들이므로 이미지를 `ImagePlus` 형식에서 `ImageProcessor`로 변환해줘야 합니다.
  * `ImageProcessor`라는 이름만 보면 뭔가 계산을 대신 해줘야 할 것 같지만, 실상은 `ImagePlus` 의 `Field` 중 하나이고, **이미지의 2D데이터 + 통계데이터 + 조작을 위한 `Method`**를 포함한 것이 `ImageProcessor` 입니다. 3D 이상이라 볼 수 있는 `stack` 관련한 데이터는 `ImageProcessor`에 포함되지 않았으며, 이건 `ImageStack`에 있습니다.
  * `ImageProcessor`로 2D 정보만 추린 후, 여기에서 통계정보를 얻는 명령이 `getStatistics()`입니다. 
* 03_inspect_03statics_01basic.py
```python
# 이미지 통계 정보 추출
from ij import IJ
from ij.process import ImageStatistics as IS

# 떠 있는 이미지 캡처
imp = IJ.getImage()  # ImagePlus : title, dimension 등 이미지 정보를 포함.
  
# ImageProcessor 호출
ip = imp.getProcessor()  
  
options = IS.MEAN | IS.MEDIAN | IS.MIN_MAX  
# getStatistics: Calculates and returns uncalibrated (raw) statistics for the specified image, including histogram, area, mean, min and max, standard deviation and mode. 
# IS.getStatistics: https://imagej.nih.gov/ij/developer/api/ij/process/ImageStatistics.html#getStatistics-ij.process.ImageProcessor-int-ij.measure.Calibration-
stats = IS.getStatistics(ip, options, imp.getCalibration())
  
  
# 통계 데이터 출력  
print "Image statistics for", imp.title
print "Mean:", stats.mean  
print "Median:", stats.median  
print "Min and max:", stats.min, "-", stats.max       
```
<br>

* 03_inspect_03statics_02multiimgs.py
```python
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
    print "Processing", filename
    fullpath = os.path.join(folder, filename)
    print "fullpath", fullpath  
    imp = IJ.openImage(fullpath)  
    if imp is None:  
      print "Could not open image from file:", filename
      continue  
    mean, median, min, max = getStatistics(imp)  
    print "Image statistics for", imp.title  
    print "Mean:", mean  
    print "Median:", median  
    print "Min and max:", min, "-", max  
  else:  
    print "Ignoring", filename
```
<br>

* 03_inspect_04iterpixels.py
```python
# pixel 단위 정보 추출
from ij import IJ 
from sys.float_info import max as MAX_FLOAT

# 떠 있는 이미지 캡처
imp = IJ.getImage()

# ImageProcessor에 담긴 정보를 float로 변환
ip = imp.getProcessor().convertToFloat()
# pixel 정보
pixels = ip.getPixels()

print "Image is", imp.title, "of type", imp.type

# pixel 최소값 구하기

# 방법 1. C언어 스타일의 for loop
minimum = MAX_FLOAT
for i in xrange(len(pixels)):
    if pixels[i] < minimum:
        minimum = pixels[i]
 
print "1. Minimum is:", minimum

# 방법 2. pixel을 list 형태로 iterate
minimum = MAX_FLOAT
for pix in pixels:
    if pix < minimum:
        minimum = pix

print "2. Minimum is:", minimum

# 방법 3. 내장(built-in)함수 사용
minimum = reduce(min, pixels)

print "3. Minimum is:", minimum
```
<br>

* 03_inspect_05loop_01map.py
```python
# map
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
```
<br>

* 03_inspect_05loop_02filter.py
```python
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

print matching
```
<br>

* 03_inspect_05loop_03reduce.py
```python
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
```
<br>

* 03_inspect_06_01subtmin.py
```python
# 이미지 전체에서 최소픽셀값 빼기
from ij import IJ, ImagePlus  
from ij.process import FloatProcessor  
  
imp = IJ.getImage()  
ip = imp.getProcessor().convertToFloat() # as a copy  
pixels = ip.getPixels()  

# Built-in 함수 사용 (min, reduce)  
# pixels를 훑으며 min 적용
minimum = reduce(min, pixels)  
  
# Method 1: for loop을 적용해서 모든 pixel 값을 직접 변경 
for i in xrange(len(pixels)):  
  pixels[i] -= minimum  
# 변경된 pixel값들로 새 이미지 만들기:  
imp2 = ImagePlus(imp.title, ip)  
  
# Method 2: 모든 pixel에서 최소값을 뺀 결과를 다른 배열(pixel3)에 저장  
pixels3 = map(lambda x: x - minimum, pixels)  
# 배열로부터 이미지 만들기  
ip3 = FloatProcessor(ip.width, ip.height, pixels3, None) # None: color  
imp3 = ImagePlus(imp.title, ip3)  
  
# Show the images in an ImageWindow:  
imp2.show()  
imp3.show()  
```
<br>

* 03_inspect_06_02cntaboveth.py
```python
# threshold 이상 pixel 갯수 세기
from ij import IJ

imp = IJ.getImage()
ip = imp.getProcessor().convertToFloat()
pixels = ip.getPixels()

# 평균값 계산: 총합을 pixel 수로 나누기
mean = sum(pixels)/len(pixels)

# 평균 이상 pixel 수 세기
n_pix_above = reduce(lambda count, a: count + 1 if a > mean else count, pixels)

print "Mean value:", mean
print "%5.2f %% pixels above mean" % (n_pix_above/float(len(pixels)) *100)
```
<br>

* 03_inspect_07_pxfilter.py
```python
# pixel value로 filtering
from ij import IJ

imp = IJ.getImage()
ip = imp.getProcessor().convertToFloat()
pixels = ip.getPixels()

# 평균값 계산
mean = sum(pixels)/len(pixels)

# 평균값 이상 pixel의 index를 list로 저장
above = filter(lambda i: pixels[i] > mean, xrange(len(pixels)))
print "Number of pixels above mean value:", len(above)

# 평균값 이상 pixel들의 center of mass 계산

# image width : pixel의 위치 파악에 활용.
width = imp.width

# Method 1: for loop
xc = 0
yc = 0
for i in above:
    xc += i % width # index i pixel의 x 좌표
    yc += i // width # index i pixel의 y 좌표
xc = xc/len(above)
yc = yc/len(above)
print xc, yc

# Method 2: sum과 map 사용
xc = sum(map(lambda i: i%width, above)) / len(above)
yc = sum(map(lambda i: i/width, above)) / len(above)
print xc, yc

# Method 3: list "above"를 단 한번만 iterate
xc, yc = [d/len(above) for d in reduce(lambda c, i: [c[0] + i % width, c[1] + i / width], above, [0, 0])] 
print xc, yc

# Method 4: list "above"를 단 한번만 iterate하지만 더 깔끔하고 성능 좋게
from functools import partial

def accum(width, c, i):
    """ index가 i인 X, Y 좌표들을 list c로 수집 """
    c[0] += i % width
    c[1] += i / width
    return c

xc, yc = [d/len(above) for d in reduce(partial(accum, width), above, [0, 0])]
print xc, yc
```
<br>
