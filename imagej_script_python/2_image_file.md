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
* Image File은 `pixel`로 이루어진 그림 외에도 여러 정보를 담고 있습니다.  
  가로세로 몇 개의 `pixel`로 구성되어 있는지, `Greyscale`은 몇 단계로 구성되어 있는지 등입니다.  
* Image Processing의 근본이 되는 데이터이므로, 이 정보들을 확인하는 방법을 알아봅시다.  

#### 2.2.1. GUI  
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
  `Bits per pixel`과 `Display range`는 한 `pixel`이 담을 수 있는 데이터의 크기를 말합니다.  
* n bit는 <img src="https://latex.codecogs.com/gif.latex?2^n" />개의 정보를 담을 수 있으므로, 8 bit는 한 `pixel`의 데이터를 <img src="https://latex.codecogs.com/gif.latex?2^8" /> = 256 단계로 표현할 수 있습니다.  
  따라서 `Display range`는 0(black)-255(white)까지의 값을 가질 수 있습니다.  

* 이 외에도 `Channels`, `Slices`, `Frames` 속성이 있으며 각기 다음과 같은 의미를 가집니다.  
  `Channel`: 하나의 `pixel`을 몇 가지의 데이터로 표현하는지. ex) 3개의 `channel`인 경우 흔히 `RGB`로 표현합니다.  
  `Slices`: 입체적인 시료를 여러 층으로 나누어 분석할 때 몇 개의 층으로 분석했는지.  
  `Frames`: 몇 장의 연속왼 이미지를 합쳤는지. ex) 동영상을 구성하는 이미지 수.
* `Channels`, `Slices`, `Frames` 속성은 `[Image] > [Properties...]` 에서 다음과 같이 확인 가능합니다.  
![image_6](/imagej_script_python/images/2_image_6.PNG)
<br>  

* 다른 예제를 통해 복잡한 이미지의 기본 정보를 살펴봅시다.  
* `[File] > [Open Samples]`에서 `mitosis.tif`를 선택합니다.  
  2 `channel`, 5 `slice`, 51 `frames`를 가진 171 x 196 image 입니다.  
![image_7](/imagej_script_python/images/2_image_7.PNG)
<br>  

* `Image Info`: 파일명, 이미지 크기, `Bits per pixel`, `Frame` 관련 정보가 보입니다.  
![image_9](/imagej_script_python/images/2_image_9.PNG)
<br>  

* `Image Properties...`: `Channels`, `Slices`, `Frames` 정보가 보입니다.   
![image_8](/imagej_script_python/images/2_image_8.PNG)
<br>  

#### 2.2.2. `ImageJ Python` Script.  
* 우리의 목적은 `python` script를 이용해서 이미지를 처리하는 것입니다.  
* `python` 명령어를 이용해서 이미지에 드러난 형상과 `pixel` 데이터를 처리하는 연습을 해 보겠습니다.  
* 다시 `Boats`를 화면에 띄우고 script 창을 열어봅시다. `[File] > [New] > [Script..]`를 클릭하면 됩니다.  
![image_3](/imagej_script_python/images/2_image_3.PNG)
<br>  

* 단축키 `[`를 누르면 한 번에 아래와 같은 창을 띄울 수 있습니다.  
* `ImageJ`는 상당히 많은 언어를 제공합니다. [[상세링크](https://imagej.net/Scripting)]  
  우리는 `python`을 이용한 스크립트를 작성할 것이므로 이 중에서 `python`을 선택합시다.  
![image_4](/imagej_script_python/images/2_image_4.PNG)
<br>  


* 엄밀히 말하면, `ImageJ`에서 지원하는 것은 `Python`이 아니라 `Jython`입니다.   
  `Jython`은 `JAVA` 플랫폼에서 `Python`을 구현한 것으로, `JAVA` class를 불러올 수 있습니다. [[Link](https://jythonbook-ko.readthedocs.io/en/latest/LangSyntax.html)]  
* `ImageJ` 자체가 `JAVA`로 구축되어 있으므로 이를 활용하기 위해 `Jython`을 택한 것으로 판단되며,  
  모듈 불러오기(`import`) 정도만 다를 뿐 전반적으로 `python`의 문법을 따릅니다. [[Link](https://imagej.net/Jython_Scripting)]  
  
* script 창에 아래와 같은 명령을 입력하고 실행해 봅시다.  
  실행 단축키는 `Ctrl + R` 입니다.  
![image_5](/imagej_script_python/images/2_image_5.PNG)  
<br>  

#### 2.2.3. `ImageJ Python` Script 설명.  
 
1. package `ij`로부터 `IJ`를 불러옵니다.  
    ```python 
    from ij import IJ
    ```  
    * `imagej`가 제공하는 package `ij` 안에는 `IJ`외에도 다양한 `class`가 있습니다. [[Link](https://javadoc.scijava.org/ImageJ1/ij/package-summary.html)]  
    이 중 지금 우리가 호출할 명령어는 `IJ` 안에만 있으므로 다른 것들은 두고 `IJ`만 불러오는 것입니다.  
  
2. 현재 열려 있는 그림을 잡아옵니다.  
    ```python 
    imp = IJ.getImage()
    ```  
    * `IJ.getImage()`는 열려 있거나 마우스가 최근에 클릭한 이미지를 데이터로 메모리에 담는 명령입니다.  
      `imp =`이 앞에 있으므로, 지금 열린 `Boat` 이미지를 통째로 `imp`라는 변수에 넣겠다는 뜻입니다.  
    * 이제 `imp`에서 읽는 정보는 `Boat` 이미지의 정보이고, `imp`를 수정하면 `Boat`이미지가 수정됩니다.  
    
3. 그림의 정보를 출력합니다.  
    ```python 
    print(imp)
    ```  
    * `python`의 `print()`명령은 ()안에 담긴 변수의 내용물을 출력하라는 뜻입니다.  
      예를 들어 `a = 1` 이라고 선언한 뒤에 `print(a)`를 하면 `a`에 담긴 `1`을 출력합니다.  
    * 여기서는 `imp`에 담긴 내용을 출력하라는 명령이므로 아래 창에 출력된 것 처럼  
      `img["boats.gif" (-5), 8-bit, 720x576x1x1x1]` 이라는 결과물이 나옵니다.  
      * `img` : "image data이고, 상세 정보는 []와 같음".  
      * `"boats.gif"` : 파일명  
      * `(-5) : ID  
      * `8-bit` : `pixel`의 data level (<img src="https://latex.codecogs.com/gif.latex?2^8" /> = 256)  
      * `720x576` : `width` x `height`  
      * 첫번째 `x1` : `channels`    
      * 두번째 `x1` : `slices`  
      * 세번째 `x1` : `frames`        
    * `width`, `height`, `channels`, `slices`, `frames` 는 이미지 데이터에 접근하는 주소가 됩니다.  
 <br>  

### 2.3. Image Meta Data 읽기.  
* Image Data가 Image가 어떻게 구성되어 있는지에 대한 정보라면,  
  Image Meta Data는 Image가 어떻게 형성되어 있는지에 대한 정보입니다.  
* `SEM`이나 `TEM`같은 현미경 사진 분석에 중요한 nm/pixel, 논문 작성시 필요한 가속전압 등이 있습니다.  

#### 2.3.1. TEM Image (`.dm3`) 
* `ImageJ`에서는 `Gatan Digital Micrograph`의 `dm3` format을 지원합니다.  
* 별도의 옵션이나 설치 없이 `[File] > [Open]`을 통해 `dm3`파일을 열 수 있고,  
  `Show Info`를 하면 다음과 같은 meta data 전체를 볼 수 있습니다.  
* `Resolution`, `Pixel size`, `Voltage`, `Magnification`등의 정보가 보입니다.  
![image_10](/imagej_script_python/images/2_image_10.PNG)  

#### 2.3.2. SEM Image (`.tif`) 
* `ImageJ`에서 `.tif`파일을 연 후, `Show Info`를 하면 `Resolution`과 `Pixel Size`정도만 보입니다.  
![image_14](/imagej_script_python/images/2_image_14.PNG)  
<br>  

* `ImageJ`에서 `tif`의 meta data 전체를 보기 위해서는 별도의 플러그인을 설치해야 합니다.    
* [다운로드 링크](https://imagej.nih.gov/ij/plugins/tiff-tags.html)에서 `tiff_tags.jar`를 다운받은 후 `ImageJ`를 재시작합니다.  
* 그리고 `[Plugins] > [TIFF Tags]`를 선택하면 파일 열기 창이 뜨는데, 여기에서 파일을 선택합니다.  

![image_11](/imagej_script_python/images/2_image_11.PNG)  
<br>  

* 그리고 작은 창에서 한 줄에 몇 글자를 보여줄 지를 선택하면,  
![image_13](/imagej_script_python/images/2_image_13.PNG)  
<br>  

* 아래와 같은 창이 뜨는데, **모든 중요 정보가 한 줄로 나타나서 별로 유용하지 않아 사용을 권하지 않습니다.**
![image_15](/imagej_script_python/images/2_image_15.PNG)  
<br>  

