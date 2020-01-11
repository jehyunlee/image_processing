---
title: 0. Readme
categories:
  - ImageJ
  - Cookbook
comments: false
thumbnail: /thumbnails/ImageJ-Cookbook/cookbook_paik.jpg
date: 2020-01-11 20:52:00
---
## 0.0. `ImageJ` Cookbook

* 코딩에서 **Cookbook**이란, 제목처럼 실제로 사용할 수 있는 코드 모음입니다.

  ![ ](cookbook.jpg)

  <br>

* 음식을 배울 때 재료의 특성과 칼질의 기초부터 배울 수도 있겠지만 주말의 허기를 달래는데 요리사 자격증까지 필요하진 않습니다. 

* 인터넷 블로그와 유튜브에 널린 레시피처럼, `ImageJ`의 스크립트 창을 열고 `python` 코드 몇 줄을 `Ctrl+C/V`하고 살짝 고쳐 원하는 결과를 얻을 수 있는 코드를 모아두려 합니다.

* [`ImageJ Tutorial`](https://jehyunlee.github.io/categories/ImageJ/Tutorial/)의 [`5. Python Script 작성`](https://jehyunlee.github.io/2019/12/19/ImageJ-tutorial-5-Script/)까지 읽어보신 분들은 아래 코드를 사용하실 수 있으리라 생각합니다.

* 좋은 `ImageJ` `Cookbook`을 발견하시면 [이메일](jehyun.lee@gmail.com)로 제보 부탁드립니다. 아래 레퍼런스에 추가하고 유용한 내용은 포스팅으로 추가해서 공유하겠습니다.

  

**Reference**

> [ImageJ Cookbook](https://imagej.net/Cookbook#Installing_the_Cookbook_plugins) 
> [ImageJ for Microscopy](https://www.future-science.com/doi/10.2144/000112517?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub%3Dwww.ncbi.nlm.nih.gov&)
> 
> [ImageJ + Python Cookbook](http://wiki.cmci.info/documents/120206pyip_cooking/python_imagej_cookbook#threshold_to_create_a_mask_binary)



## 0.1. `ImageJ` Cookbook Installation

* `ImageJ`에서 자체적으로 제공하는 [Cookbook](https://imagej.net/Cookbook#Installing_the_Cookbook_plugins) 이 있습니다.
* 예를 들면 [Particle Analysis](https://imagej.net/Particle_Analysis) 는 어떤 절차를 거쳐 진행되는지 예시를 보여주고 `ImageJ`에 원클릭으로 실행할 수 있는 메뉴를 제공합니다.
* 파라미터와 절차가 본인의 이미지에 맞게 설정된 것이 아니므로 원클릭 실행에는 큰 기대를 하기 힘들지만 절차를 보고 공부하기는 좋습니다.
* [공식 홈페이지](https://imagej.net/Cookbook)에 실린 내용을 소개드립니다.

1. [`ImageJ`를 설치](https://jehyunlee.github.io/2019/12/15/ImageJ-tutorial-1-ImageJInstallation/)합니다.

2. 업데이트를 위해 `Help > Update...` 로 들어갑니다.

  ![](0_readme_1.PNG)
  <br>

3. 좌측 하단 `Manage update sites`에서 `Cookbook`을 선택하고, `Close`를 누릅니다.
  * 어떤게 있나 살펴보셔도 좋습니다. 
  * `Tensorflow`와 `TEM suite`라는 것도 있습니다.
    ![](0_readme_2.PNG)
    <br>

4. 설치되는 동안 잠시 기다립니다.

  ![](0_readme_3.PNG)
  <br>

5. `ImageJ`를 재시작하면 `Cookbook` 탭에 연결된 기능들을 볼 수 있습니다.

  ![](0_readme_4.PNG)
  <br>

6. [홈페이지](https://imagej.net/Cookbook#Installing_the_Cookbook_plugins) 에서 제공하는 설명과 내 이미지에 실행한 결과를 비교하며 공부합니다.
  * [Particle Analysis](https://imagej.net/Particle_Analysis) 예제 페이지입니다.

  ![](0_readme_5.PNG)
  <br>


