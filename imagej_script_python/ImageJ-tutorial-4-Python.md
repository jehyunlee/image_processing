---
title: 4. Python Basic
categories:
  - ImageJ
  - Tutorial
comments: false
thumbnail: /thumbnails/ImageJ-Tutorial/4_python_1.PNG
date: 2019-12-19 11:59:13
---
### 4.1. `Python` 문법을 공부하는 이유

* `ImageJ`에서 활용하는 `jython`은 `Java Virtual Machine (JVM)` 위에서 `python`을 구현한 것입니다.  
<br>
* 주로 web 환경에 많이 사용되는 `JVM`과 `python`의 연동이 자유로워 `Java Class`와 `.jar` 파일을 아무런 변환이나 노력 없이 그대로 끌어다 사용할 수 있다는 장점이 있습니다. `ImageJ`의 개발자들 역시 `Java` 로 제작해둔 라이브러리를 `python`명령어를 이용해 활용할 수 있게 하기 위해 `jython`을 택했다고 보입니다.  
<br>
* `ImageJ`의 `jython` script는 `java` 라이브러리를 불러오지만 `python`문법으로 실행합니다. `python` 문법 전체를 모두 담을 수는 없지만 `ImageJ` script를 작성하고 이해하는 데 필요한 기본 명령어를 정리했습니다. `python` 문법과 체계가 더 알고싶다면 아래의 [점프 투 파이썬](https://wikidocs.net/book/1) 링크를 참조하시기 바랍니다.

**Reference**

> [Jython Runner's Home](https://jython.tistory.com/)  
> [Definite Guide to Jython](https://jython.readthedocs.io/en/latest/)  
> [점프 투 파이썬](https://wikidocs.net/book/1)  
> [A Fiji Scripting Tutorial #3. Inspecting properties and pixels of an image](https://www.ini.uzh.ch/~acardona/fiji-tutorial/#s3)  

### 4.2. `import`: 모듈 불러오기

![ ](4_python_1.PNG)
* 우리는 집 안에서 비바람을 피할 뿐 아니라 식사, 빨래, 게임, TV와 인터넷 사용 등 많은 일을 하지만 집 자체가 이러한 기능들을 제공하는 것은 아닙니다.  집은 텅 빈 공간일 뿐이고, 여기에 밥솥, 전자렌지, 냉장고, 식기가 들어와야 부엌이 갖추어지고 세탁기와 건조기가 들어와야 빨래를 하고 건조를 시킬 수 있습니다.  
<br>
* [앞서](https://jehyunlee.github.io/2019/12/16/ImageJ-tutorial-3-DevEnv/) 설치한 `miniconda(anaconda)`는 상하수도와 전기, 가스만 붙어있는 텅 빈 집이나 마찬가지입니다. 빈 집에서 모든 가전제품을 스스로 만들 수도 있겠지만, 그것보다 판매되는 제품을 구매하는 것이 훨씬 경제적입니다. 이렇게 다른 사람이 만든 모듈을 불러오는 과정을 `import`라고 합니다.  
<br>
* 이처럼 특정 기능을 구현해놓은 것을 부르는 이름으로  `module`, `package`, `library` 가 있습니다. [세세하게 분류하는 분](https://www.quora.com/What-is-the-difference-between-Python-modules-packages-libraries-and-frameworks)도 있습니다만 사용자 입장에서는 많은 경우 혼용해서 사용하며, 의사소통상 큰 무리는 없습니다.  

#### 4.2.1. 모듈 전체를 불러오기

* 모듈 안에는 함수와 같은 기능이 여럿 포함되어 있을 수 있습니다.  

* 모듈 전체를 불러올 때는 다음과 같이 불러옵니다.
  ```python
  import [모듈 이름]
  ```

*  `module1` 이라는 모듈에 두 수의 합을 출력하는 `sumf()`라는 함수가 있다면, 다음처럼 사용할 수 있습니다.  
  ```python
  import module1
  
  ans = module1.sumf(3, 4) # ans 변수에 3 + 4 = 7 저장됨.
  ```

* 함수를 부를 때마다 `module1.`을 매번 앞에 써줘야 하기 때문에 번거롭습니다.  
  `module1` 대신 `m1`이라고 부르기로 하겠습니다.
  ```python
  import module1 as m1
  
  ans = m1.sumf(3, 4) # ans 변수에 3 + 4 = 7 저장됨.
  ```

* `import [모듈 이름] as [짧은 이름]` 형식을 사용해서 번거로움을 줄일 수 있습니다.

#### 4.2.2. 함수를 따로 부르기

* 함수를 사용하기 위해서 모듈 이름을 매번 부르는 것은 귀찮은 일입니다.  

* `from [모듈 이름] import [함수 이름]`을 이용해서 함수 이름만 사용할 수 있습니다.
  ```python
  from module1 import sumf
  
  ans = sumf(3, 4) # ans 변수에 3 + 4 = 7 저장됨.
  ```

* 함수 이름도 짧게 줄일 수 있습니다.
  ```python
  from module1 import sumf as sf
  
  ans = sf(3, 4) # ans 변수에 3 + 4 = 7 저장됨.
  ```

* 모듈에 함수가 여럿 있고 이들을 모두 부르고 싶다면 `from [모듈 이름 ] import *`을 사용하면 됩니다.

  **※ 주의 ※** 여러  `module`을 이렇게 부르면, 함수 이름이 겹칠 때 마지막 함수만 사용 가능합니다.

### 4.3. `print`: 출력하기

* 계산 결과나 문자열을 출력할 때 사용하는 함수입니다.

* `python` 을 최근에 3.x 버전으로 학습하신 분은 `print()` 명령으로 알고 계실 테지만,
  `jython`은 기본적으로 `python 2.7`버전을 사용하기 때문에 기본적으로 `print [출력 내용]`을 사용합니다.
  
* 특이하게도 `python` 3.x 버전의 `print()` 형식도 지원하지만, 간혹 출력이 깔끔하지 못한 경우가 있으니 2.7 버전의 사용법을 익숙하게 합시다.
  
  ```python
  a = 3.141592
  print a    # a 내용 출력: "3.141592"
  print 'a'  # 문자 a를 출력: "a"
  print 'a=', a # 문자열과 a의 내용을 붙여서 출력: "a= 3.141592"
  ```

* `%`를 사용해서 출력 형식을 지정할 수 있습니다.
  ```python
  a = 3.141592
  print '%d' % a     # 정수형으로 출력합니다: "3"
  print '%3d' % a   # 총 3자리 정수를 출력, 빈 자리에 빈칸을 출력합니다: "  3"
  print '%03d' % a   # 총 3자리 정수를 출력, 빈 자리에 0을 붙입니다: "003"
  
  print '%f' % a     # 소수형으로 출력합니다: "3.141592"
  print '%1.3f' % a  # 소수점 3자리까지만 출력합니다: "3.142"
  print '%7.3f' % a  # 총 7글자, 소수점 3자리까지만 출력합니다: "  3.142"
  print '%07.3f' % a  # 총 7글자, 소수점 3자리까지 빈칸을 0으로 출력합니다: "003.142"
  ```

* 줄 바꿈 문자(`\n`), 탭 문자(`\t`) 등을 사용해서 간단한 틀에 맞춘 출력을 할 수 있습니다.
  ```python
  print 'The answer is : %d\t(%1.2f)\nOthers are wrong!' % (1, 3.141592)
  
  # 출력결과:
  # The answer is 1 :       (3.14)
  # Others are wrong!
  ```

### 4.4. `if`, `elif`, `else`: 조건문

* 특정 조건을 만족하는 부분만 처리하는 등, 조건에 행동을 다르게 할 때 사용합니다.
* `if [조건]:` 밑에 조건을 만족할 때 실행할 행동을 들여쓰기를 해서 작성합니다.
  ```python
  if 조건문:
      수행할 문장1
      수행할 문장2
  ```
  
* `if` 조건을 만족하지 않을 경우 실행할 행동을 `else`문에 넣어줍니다.
  ```python
  money = True
  if money:
      print "Taxi!"
  else:
      print "Walk!"
      
  # 출력결과:
  # Taxi!
  ```

* 이렇게 해서 결과를 비교해 봅니다.
  ```python
  money = False
  if money:
      print "Taxi!"
  else:
      print "Walk!"
      
  # 출력결과:
  # Walk!
  ```

* 조건문은 비교연산자로 표현할 수도 있습니다.

| **비교연산자**  |       **설명**        |
| :-------------: | :-------------------: |
|      x < y      |    x가 y보다 작으면 참     |
|      x > y      |    x가 y보다 크면 참     |
|     x == y      |     x와 y가 같으면 참      |
|     x != y      |   x와 y가 같지 않으면 참   |
| x <= y | x가 y보다 작거나 같으면 참 |
| x >= y | x가 y보다 크거나 같으면 참 |

* `and`, `or`, `not` 연산자도 있습니다.

| **연산자**  |       **설명**        |
| :-------------: | :-------------------: |
|      x or y      |    x와 y 중 하나만 참이면 참     |
|      x and y      |    x와 y 모두 참이어야 참     |
|      not x      |    x가 거짓이면 참이다     |

* 여러 조건이 있는 경우 `elif`로 조건을 추가할 수 있습니다.
  `elif`는 `if`와 `else` 사이에 여러 개가 올 수 있지만 위에서부터 순차적으로 조건을 검토해서 적용하는 것을 유념해야 합니다.
  ```python
  money = 3000
  if money > 10000:
      print "Taxi!"
  elif money > 1000:
      print "Bus!"
  else:
      print "Taxi!"
  
  # 출력결과:
  # Bus!
  ```

* `if`, `elif`, `else`는 여러 층으로 적용할 수 있습니다.
  
  ```python
  pocket = ['paper', 'handphone']
  card = True
  if 'money' in pocket:
      print 'Taxi!'
  else:
      if card:
          print '택시를 타고 가라'
      else:
          print '걸어가라'
          
  # 출력결과:
  # Taxi!
  ```





print()
if, elif, else
for, while
try, except, finally

* 연산자
//, %, +=, -= 등등

* 함수
lambda