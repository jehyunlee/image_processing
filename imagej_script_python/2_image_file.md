## 2. Image File 구조  
* 여러분이 다룰 Image File의 구조를 간략하게 살펴보겠습니다.  
* 최대한 간결하게 필수적인 지식만 전달하고자 합니다.  
* 자세한 정보를 원하시면 공식 매뉴얼을 참고하시기 바랍니다 : [[Link](https://imagej.nih.gov/ij/docs/guide/146-7.html#toc-Section-7)]

### 2.1. Image File 읽기.  
* `ImageJ`에서는 다른 프로그램처럼 `[File] > [Open]`을 통해서 이미지 파일을 열 수 있습니다.  
* 각자 파일은 조금 나중에 열어보기로 하고, 여기서는 동일한 설명을 위해 같은 파일을 열어보겠습니다.  
* `ImageJ`에서 제공하는 Sample Image를 다음과 같이 열 수 있습니다.  
* `[File] > [Open Samples]`로 가면 다양한 그림들이 있는데, 여기서 `Boats (356K)`를 선택합시다.  

![image_0](/imagej_script_python/images/2_image_0.PNG)
<br>  

### 2.2. Image File 정보 읽기.  
* 아래 왼쪽과 같이 흑백 배 사진을 보실 수 있습니다.  
* 사진 왼쪽 위를 자세히 보시면 `720x576 pixels; 8-bit, 405K`라는 정보가 나와 있습니다만 조금 더 자세히 알아봅시다.  
* `[Image] > [Show Info]`를 클릭하시면 이미지의 전체적인 정보를 보실 수 있습니다.  
* 이미지 창에서 `Ctrl + I` 단축키를 입력하셔도 됩니다.  
![image_1](/imagej_script_python/images/2_image_1.PNG)
<br>  

* 그럼, 아래와 같은 Image File의 정보가 요약된 창이 뜹니다.  
![image_2](/imagej_script_python/images/2_image_2.PNG)
<br>  

* `Title` 은 파일명, `Width`은 이미지의 폭, `Height`는 이미지의 높이, `Size`는 파일 크기를 말하며,  
  조금 아래에 있는 `Bits per pixel`과 `Display range`는 한 `pixel`이 담을 수 있는 데이터의 크기를 말합니다.  
* n bit는 <img src="https://latex.codecogs.com/gif.latex?2^n" />개의 정보를 담을 수 있으므로, 8 bit는 한 `pixel`의 데이터를 <img src="https://latex.codecogs.com/gif.latex?2^8" /> = 256 단계로 표현할 수 있습니다.  
* 따라서 `Display range`는 0(black)-255(white)까지의 값을 가질 수 있습니다.  

* 이 외에도 `Channels`, `Slices`, `Frames` 속성이 있으며 각기 다음과 같은 의미를 가집니다.
  `Channel`: 하나의 `pixel`을 몇 가지의 데이터로 표현하는지. ex) 3개의 `channel`인 경우 흔히 `RGB`로 표현합니다.  
  `Slices`: 입체적인 시료를 여러 층으로 나누어 분석할 때 몇 개의 층으로 분석했는지.  
  `Frames`: 몇 장의 연속왼 이미지를 합쳤는지. ex) 동영상을 구성하는 이미지 수.
* `Channels`, `Slices`, `Frames` 속성은 `[Image] > [Properties...]` 에서 다음과 같이 확인 가능합니다.  
![image_6](/imagej_script_python/images/2_image_6.PNG)
<br>  

