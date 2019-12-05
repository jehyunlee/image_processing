## 3. ImageJ에서 Python으로 Image File 다루기

### 3.1. Image 불러오기
* [앞서 드린 설명](https://github.com/jehyunlee/image_processing/blob/master/imagej_script_python/2_image_file.md#21-image-file-%EC%9D%BD%EA%B8%B0)에 따라 `Boat.gif` 이미지를 띄웁니다.  

### 3.2. ImageJ 개발창 띄우기
* [앞서 드린 설명](https://github.com/jehyunlee/image_processing/blob/master/imagej_script_python/2_image_file.md#222-imagej-python-script)을 따라 script 창을 띄웁니다.  
* `New_.py`라는 파일이 자동으로 생성되며, 저장되지 않았다는 뜻으로 `*`이 파일 이름 앞에 붙어있습니다.  
* 본인이 작업할 위치에 가서 파일명을 `01_imgfile_01.py`라고 저장합시다.

### 3.3. ImageJ 개발환경 설정하기 
#### 3.3.1. `Notepad++` 설치
* `python`등의 프로그래밍 언어는 굉장히 많은 명령어와 변수를 다루어야 하기 때문에 `통합 개발 환경 (IDE: Integrated Development Environment)`를 통한 명령어와 변수의 자동 완성 기능을 제공하고 있습니다.  
* 그러나 `ImageJ`에서 제공하는 개발환경은 이 점에서 매우 **불편**하기 때문에 다른 환경을 사용하고자 합니다.  
* [`notepad++`](https://en.wikipedia.org/wiki/Notepad%2B%2B)를 [다운로드](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.1/npp.7.8.1.Installer.exe)받아 설치합니다. 앞으로 개발은 여기에서 진행하겠습니다.  
* `npp.버전.installer.exe`를 실행 후 `[다음]`만 반복해서 설치하셔도 됩니다.
**※ 주의 ※** 사용자 정의 설치를 하는 것은 좋으나 `Auto-completion Files`는 선택을 유지하고 있어야 합니다.   
![img](https://github.com/jehyunlee/image_processing/raw/master/imagej_script_python/images/3_file_1.PNG)  

#### 3.3.2. `Notepad++` 코딩 테스트  
* [위에서](https://github.com/jehyunlee/image_processing/new/master/imagej_script_python#32-imagej-%EA%B0%9C%EB%B0%9C%EC%B0%BD-%EB%9D%84%EC%9A%B0%EA%B8%B0) 저장한 `01_imgfile_01.py`를 `Notepad++`에서 엽니다.  
* 언어를 `Python`으로 설정해줍니다. `언어` > `P` > `Python`을 체크해주세요.   
![img](https://github.com/jehyunlee/image_processing/raw/master/imagej_script_python/images/3_file_2.PNG)  

* i만 입력해도 pull-down 메뉴가 뜨면서 `python`에서 사용하는 i로 시작하는 명령어 등이 펼쳐지는 것을 보실 수 있습니다.  
* 이들 중 하나를 골라서 입력하셔도 좋고, 이걸 보고 오타를 줄이셔도 좋습니다.  
![img](https://github.com/jehyunlee/image_processing/raw/master/imagej_script_python/images/3_file_3.PNG)  

