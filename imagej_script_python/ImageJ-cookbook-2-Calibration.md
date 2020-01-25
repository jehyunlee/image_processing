---
title: 2. Image Calibration
categories:
  - ImageJ
  - Cookbook
comments: false
thumbnail: /thumbnails/ImageJ-Cookbook/2_cal_2.jpg
date: 2020-01-18 18:30:00
---
**Reference**

> [Earth Analysis Techniques: Introduction to Image Analysis](https://serc.carleton.edu/earth_analysis/image_analysis/introduction/index.html)

### 2.1. Calibration의 의미

* [이미지 파일의 구조](https://jehyunlee.github.io/2019/12/16/ImageJ-tutorial-2-ImageFileStructure/)에 대한 글에서, 이미지는 2차원 공간상에 위치한 `pixel`의 집합이라고 말씀드렸습니다.

* 대개 `pixel` 하나당 흑백(`Grayscale`) 이미지의 경우 숫자 하나가, 컬러 이미지의 경우 숫자 3개가 RGB `channel`의 형태로 할당되어 있습니다.

* 그러나 이미지에 찍힌 대상의 실제 크기는 `pixel`과 다른, `meter` 등의 단위로 이루어져 있습니다. 이를 보정하는 과정을 `calibration`이라고 하며, `scale`을 `pixel`단위 길이나 넓이에 곱합니다.

  * `ImageJ`에서 이미지를 열고 포인터를 그림 위에 올리면, 메인 창에 `x`, `y`좌표와 함께 `pixel`값이 나옵니다. 
    ![ ](2_cal_1.PNG)    
  * 그러나 어떤 이미지는 `ImageJ` 메인 창의 `x`, `y`좌표, `pixel`값에 괄호`()`가 붙어있습니다.
  * 아래 예제의 [원본은 여기에서 다운로드](2_cal_2.tif) 받을 수 있습니다.
    ![ ](2_cal_2.PNG)        
  * 괄호 안의 값은 `pixel`단위, 괄호 밖의 값은 보정된(`calibrated`) 실제 길이입니다.
  * 이미지 우측 하단 $ 2\ \mu\text{m} $  scale bar의 길이는 484 px 입니다. 
  * 메타데이터로부터 얻은 `scale`이 4.13 nm/px이므로, 확인을 위해 곱해보면 $ 484 \times 4.13 = 1998.92\ \text{nm} $ 이므로 $ \approx 2 \mu\text{m} $ 입니다.
<br>
* `ImageJ` `Calibration`은 크게 두 가지로 나뉘어집니다.
  * **Spatial Calibration** : `x`, `y`등 길이 방향을 보정합니다.
  * **Density Calibration**: `pixel`값을 보정합니다.

### 2.2. Calibration의 활용

* Calibration이 된 이미지를 이용해 측정해봅시다.
  * `DEM`: Digital Elevation Model이라는 종류의 데이터가 있습니다. 
  * 이미지 형식이지만 `pixel`에 담긴 값은 해당 위치의 고도를 의미합니다.
  * 제한된 값(8 bit Grayscale 이미지: 0~255) 값만으로 훨씬 넓은 범위의 고도를 파악해야 하므로 `pixel`값에 scale이 적용되어 있습니다.

* [여기에서 이미지를 다운로드](2_cal_3.tif)받아 `ImageJ`에서 엽니다.

  * <b>`Image > Lookup Tables`</b>에서 `Green Blue Fire`를 선택합니다.

  * 흔히 `LUT`라고 말하는 Loopup Table은 Grayscale에 담긴 Scalar 값을 시각화할 colormap입니다.

  * 실제 값은 변경하지 않고 `ImageJ`에서 보여주는 시각적인 효과만 변경됩니다.

  * <b>`Analyze > Surface Plot`</b>을 선택하고 옵션에서 `Draw Wireframe`, `Shade`, `Draw Axis`, `Smooth`를 선택합니다. 2차원 그림이 3차원으로 변환됩니다. **z 축** 숫자를 보면 167 ~ 2408로 표시되어 있습니다. `Calibration`이 적용된 것입니다.

  * <b>`Analyze > 3D Surface Plot`</b>을 선택해도 비슷한 그림을 얻을 수 있습니다. 3D 회전을 비롯해서 `Grid Size`, `Smoothing` 등을 실시간으로 조정할 수 있는 interactive plot입니다. 여기서는 **z 축**에 `Calibration`이 적용되지 않았습니다.

    ![ ](2_cal_3.png)

### 2.3.Calibration (GUI)

#### 2.3.1. Spatial Calibration (GUI)

* 이미지의 Scale Bar를 이용하여 Spatial Calibration을 설정해 보겠습니다.

  * 메인 창에서 **Line Selection Tool**을 선택하고 Scale Bar를 따라 선을 긋습니다. 첫 지점을 클릭하고 `shift`키를 누른 채 마우스를 이동하면 포인터를 수평으로만 움직일 수 있습니다.

  * [Calibration을 적용할 이미지를 여기에서 다운로드](2_cal_2.tif)받아 `ImageJ`에서 열고, <b>`Analyze > Set Scale...`</b>을 선택하여 Scale 설정 창을 엽니다.

  * 조금 전 손으로 그었던 선의 길이가 `Distance in pixels`로 483이 나옵니다.

  * Scale Bar에 $2\ \mu \text{m} = 2000\ \text{nm}$ 라고 되어 있으므로  `Known distance`에 2000을 입력하고 `Unit of length`에 nm를 입력합니다.

  * 본 이미지에만 적용할 Calibration이므로 `Global`은 체크되지 않은 채로 놔둔 채 `OK`를 누르면 Calibration이 적용됩니다.

    ![ ](2_cal_4.png)

* 방금 설정한 Calibration을 이용하여 Particle의 지름을 측정해 보겠습니다.
  
  * 지름을 잴 Particle을 정하고, **Line Selection Tool**을 이용해서 지름에 맞춰 선을 긋습니다.
  
  * <b>`Analyze > Set Measurements`</b>에서 측정할 항목을 선택합니다. `Angle`과 `Length`는 기본으로 출력되니 추가로 얻을 값들을 선택하고, 필요 없는 값들을 선택 해제하면 됩니다.

  * <b>`Analyze > Measure`</b>를 선택하면 Results 창이 뜨고 `Length = 896.401`이 출력됩니다. Results 창에서 <b>`File > Save as...`</b>를 선택하면 `.csv`파일로 저장할 수 있습니다.
  
  * <b>`Analyze > Plot Profile`</b>을 선택하면 Particle의 지름을 가로지르는 선을 따라 Intensity Profile을 얻을 수 있습니다. 
  
    ![ ](2_cal_5.png)

* `ImageJ`에서 이미지에 Scale Bar를 삽입할 수 있습니다.

  * <b>`Analyze > Tools > Scale Bar...`</b>를 선택합니다.

  * `Scale Bar` 창에서 Calibration 단위(`nm`) 기준의 길이와 Scale Bar의 `Height`, `Font Size`, `Location` 등을 설정합니다. 설정값에 따라 이미지 위에 실시간으로 Scale Bar가 생성되니 보시면서 원하는 상태로 설정하면 됩니다.

  * $2000\ \text{nm}$ 대신 $2\ \mu \text{m}$로 출력되기를 원하시면, calibration을 $\mu \text{m}$ 단위로 진행하시면 됩니다.

    ![ ](2_cal_11.PNG)

#### 2.3.2. Density Calibration (GUI)

* Density Calibration을 위해선 다음 두 가지 사항이 필요합니다.
  1. 두 지점 이상의 `pixel`과 데이터(`value`)  쌍
  2. Density Calibration의 함수(`function`): Linear? Polynomial? Exponential?
* Density Calibration을 위한 데이터가 주어지면 좋지만, 그렇지 않은 경우 이미지 한켠의 범례(`legend`)를 이용해서라도 입력해야 합니다.

* `GeoTIFF` 이미지 데이터를 이용해서 Density Calibration을 해 보겠습니다.
  ![ ](2_cal_7.png)
  * `GeoTIFF` 형식은 지리정보(GIS)와 기상 분야에 주로 사용되며, 이미지 외에도 `map projection`, `coordinate systems`, `ellipsoids` 등의 데이터를 함께 담고 있습니다.
  * [여기에서 예제파일을 다운](2_cal_7.tif)받습니다.
  * `ImageJ`에서 파일을 열고, <b>`Analyze > Calibrate`</b>를 선택합니다.
  * `Calibrate` 창에서, 왼쪽에 `pixel` 값을 넣고 오른쪽은 이에 해당하는 `value`를 넣어줍니다.
    1. 왼쪽 공간에 0과 254를 넣습니다. 데이터 사이는 `Enter`키로 띄워줍니다.
    2. 오른쪽 공간에 -2와 45를 넣습니다. 역시 `Enter`키로 분리해 줍니다.
    3. 섭씨 온도 데이터입니다. `unit`에 해당하는 곳에 `Degrees Celsius`를 넣습니다.
    4. 1차식 데이터이므로 <b>Function </b>메뉴에서 `Straight Line`을 선택합니다.
    5. `OK`를 누르면 `Calibration Function`이 보일 것입니다.
    6. `Calibration Function`을 닫고 이미지 위에 마우스를 가져가면, 메인 창에 포인터가 위치한 지점의 x, y 좌표와 함께 value가 보입니다.
    7. 이미지를 <b>`File > Save As`</b>에서 `.tif`형식으로 저장하면 `Calibration`이 함께 저장됩니다.
    ![ ](2_cal_8.PNG)

* Density Calibration을 이용해 이미지 데이터 분석을 해 보겠습니다.
  * <b>`Analysis > Set Measurements`</b>에서 `Area`, `Mean gray value`, `Standard deviation`, `Modal gray value`, `Min & Max gray value`를 선택하고 <b>`OK`</b>를 눌러 창을 닫습니다.
  * <b>`Analysis > Measurement`</b>를 클릭하면 <b>Results</b>창이 뜹니다.
  * <b>Set Measures</b>에서 지정한 분석 결과가 담겨 있습니다.
  
  ![ ](2_cal_9.PNG)

* Scale Bar처럼 Density Calibration을 Legend로 삽입할 수 있습니다.

  * <b>`Analyze > Tools > Calibration Bar...`</b>를 선택합니다.

  * Scale Bar와 대체로 비슷하지만 `Number of Labels`, `Decimal Places`, `Zoom Factor`등 다른 인자들이 있습니다. 
  * 직접 인자를 바꿔가면서 Legend가 실시간으로 어떻게 변하는지 살펴보시기 바랍니다.

    ![ ](2_cal_10.PNG)

<br>

### 2.4.Calibration (python script)

#### 2.4.1. Spatial Calibration (python script)

* `python` script를 이용해 현재의 `Calibration`값을 확인하고, 새로운 `Calibration`을 적용하겠습니다.

* `getCalibration()`으로 현재 이미지의 `Calibration`값을 읽고,

  `calibration().pixelWidth`와 `calibration().pixelHeight`를 수정해 `Calibration`을 수정합니다.

* 마지막으로 `setCalibration()`으로 새 이미지에 바뀐 값을 저장합니다.

  * [같은 이미지](2_cal_2.tif)를 `ImageJ`에 띄워 놓고, script 창을 열고 아래 코드를 붙여넣고 실행합니다.

  ```python
  from ij import IJ, ImagePlus
  from ij.plugin import Duplicator
  
  # 1. Get Open Image
  imp = IJ.getImage()
  
  # 2. Get Initial Calibration
  cal = imp.getCalibration()
  print 'before Calibration:', cal
  
  # 3. Duplicate Image
  imp2 = Duplicator().run(imp)
  
  # 4. Apply New Calibration
  scale = 4.13 # nm/px
  cal.pixelWidth = scale # pixelWidth : Pixel width in 'unit's
  cal.pixelHeight = scale # pixelHeight : Pixel height in 'unit's
  cal.unit = 'nm'
  print 'after Calibration:', cal
  imp2.setCalibration(cal)
  
  # 5. Show New Image
  imp2.title = 'Calibrated'
  imp2.show()
  ```

  * 실행 결과 

  ![ ](2_cal_6.png)

  * 새 창으로 뜨는  `Calibration`이 적용된 이미지는 처음 이미지와 동일해 보입니다.
  * 그러나 Scale Bar를 따라 **Line Selection Tool**을 긋고 <b>`Analyze > Measure`</b>를 실행하면 `Length = 2007.180`이라는 값이 나옵니다.
  * `Calibration`을 적용하기 전 값은 `Length = 8.643`으로, 성공적으로 적용되었음을 알 수 있습니다.
  * 이상적으로는 `Length = 2000`이 나와야 하지만, Line Selection을 할 때 손끝에서 발생한 오차로 인해 다소 크게 측정된 것입니다.

#### 2.4.2. Density Calibration (python script)

* Density Calibration 또한 `python` script를 이용해 진행할 수 있습니다.
* 먼저, 위 `2.4.1` 코드와 실행 결과를 보면 현재의 `Calibration`을 읽어서 `cal`이라는 변수에 저장하고 출력한 결과가 `w`, `h`, `d`, `unit`, `f`, `nc`, `table`, `vunit`, `bd`로 출력됩니다. 각각의 의미는 다음과 같습니다.
* 
