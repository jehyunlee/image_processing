---
title: 1. CSV file I/O
categories:
  - ImageJ
  - Cookbook
comments: false
thumbnail: /thumbnails/ImageJ-Cookbook/cookbook.jpg
date: 2020-01-11 22:52:00
---
**Reference**
> [ImageJ + Python Cookbook](http://wiki.cmci.info/documents/120206pyip_cooking/python_imagej_cookbook#threshold_to_create_a_mask_binary)

## 1.1. Loading CSV File

* `csv` 파일을 읽는 예제입니다.

* 예제 파일은 [여기에서 다운](https://github.com/jehyunlee/image_processing/blob/master/imagej_script_python/data/loadexample.csv)받을 수 있습니다.

### 1.1.1. CSV 파일 읽어서 결과 보여주기
  ```python
  import csv
  
  filepath = r'C:\Tmp\loadexample.csv'
  f = open(filepath, 'rb')
  data = csv.reader(f, delimiter=' ')
  for row in data:
      print ', '.join(row)
  ```

  * 실행결과
    ![ ](1_csvio_1.PNG)
    <br>

#### 1.1.2. CSV 파일 읽어서 특정 컬럼을 창으로 띄워주기
  ```python
  from ij import IJ
  from util.opencsv import CSVReader
  from java.io import FileReader
   
  def readCSV(filepath):
      reader = CSVReader(FileReader(filepath), ",")
      ls = reader.readAll()
      for item in ls:
   	      IJ.log(item[2])
 
  filepath = r'C:\Tmp\loadexample.csv'
  readCSV(filepath)
  ```

  * 실행결과
    ![ ](1_csvio_2.PNG)
    <br>

### 1.2. Save as CSV File

* `csv` 파일을 쓰는 예제입니다.

#### 1.2.1. `python`방식 : `pythonic`
  ```python
  import csv
  
  f = open(r'C:\Tmp\saveexample1.csv', 'wb')
  writer = csv.writer(f)
  writer.writerow(['does this work'])
  writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
  #can chop down more
  writer.writerows(['Spam', 'Lovely Spam', 'Wonderful Spam'])
  f.close()
  ```

  * 실행결과
    ![ ](1_csvio_3.PNG)
    <br>

#### 1.2.2. Numerical data (`pythonic`)
  ```python
  import os, csv
  
  # prepare test data to write to a csv file
  data1 = range(10)
  data2 = [x * x for x in data1]
  data3 = [pow(x, 3) for x in data1]
  print data3
  
  # prepare path
  root = r"C:\Tmp"
  filename = r"saveexample2.csv"
  fullpath = os.path.join(root, filename)
  print fullpath
  
  # open the file first (if its not there, newly created)
  f = open(fullpath, 'wb')
  
  # create csv writer
  writer = csv.writer(f)
  
  # for loop to write each row
  for i in range(len(data1)):
      row = [data1[i], data2[i], data3[i]]
      writer.writerow(row)
  
  #writer.writerows([data1, data2, data3])
 
  # close the file. 
  f.close()
  ```
  * 실행결과
    ![ ](1_csvio_4.PNG)
    <br>

#### 1.2.3. `java` 활용
  ```python
  from util.opencsv import CSVWriter
  from java.io import FileWriter
  from java.lang.reflect import Array
  from java.lang import String, Class
  
  writer = CSVWriter(FileWriter(r'C:\Tmp\saveexample3.csv'), ',')
  data = Array.newInstance(Class.forName("java.lang.String"), 3)
  
  data[0] = str(11)
  data[1] = str(23)
  data[2] = str(5555)
  writer.writeNext(data)
  writer.close()  
  ```
  * 실행결과
    ![ ](1_csvio_5.PNG)
    <br>

#### 1.2.4. `java`의 `jarray` module 활용
  ```python
  from util.opencsv import CSVWriter
  from java.io import FileWriter
  from java.lang import String
  from jarray import array as jarr
  
  writer = CSVWriter(FileWriter(r'C:\Tmp\saveexample4.csv'), ',')
  header = ['x', 'y', 'z']
  jheader = jarr(header, String)
  data = [11,23,5555]
  datas = map(str, data)
  jdata = jarr(datas, String)
  writer.writeNext(jheader)
  writer.writeNext(jdata)
  writer.close()
  ```
  * 실행결과
    ![ ](1_csvio_6.PNG)
    <br>