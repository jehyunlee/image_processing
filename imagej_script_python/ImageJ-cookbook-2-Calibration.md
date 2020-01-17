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
  * 괄호 안 밖의 값은 `pixel`단위, 괄호 안의 값은 보정된(`calibrated`) 실제 길이입니다.
  * 이미지 우측 하단 $ 2\ \mu\text{m} $  scale bar의 길이는 484 px 입니다. 
  * 메타데이터로부터 얻은 `scale`이 4.13 nm/px이므로, 확인을 위해 곱해보면 $ 484 \times 4.13 = 1998.92\ \text{nm} \approx 2 \mu\text{m} $ 입니다.
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

### 2.3. Spatial Calibration (GUI)

* 이미지의 Scale Bar를 이용하여 Calibration을 설정해 보겠습니다.

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

### 2.4. Spatial Calibration (python script)

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
  cal.pixelWidth = scale
  cal.pixelHeight = scale
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

