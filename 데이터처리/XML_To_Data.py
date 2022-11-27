import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests
from urllib import parse

''' matplotlib 한글이 깨진다면 다음 명령어를 터미널에서 진행
sudo apt-get install -y fonts-nanum
sudo fc-cache -fv
rm ~/.cache/matplotlib -rf


'''
# -- 위 명령어를 사용한 후 다음 코드 실행plt.rc('font', family='NanumBarunGothic') 


import xml.etree.ElementTree as ET

def ReadDataFromXML(key, url, dataPath, year):
  key = key
  key = parse.unquote(key)
  #-- encoder key value to decoder key value

  queryParams = '?' + parse.urlencode({
    'serviceKey' : key,
    'page' : 1,
    'perPage' : 10,
    'returnType' : "XML",
  })
  #-- Set queryParams

  url = url + queryParams
  #-- Set Url

  response = requests.get(url)
  response.status_code
  #-- 200 

  with open(dataPath, "w") as f:
    f.write(response.text)
  
  campXML = ET.parse(dataPath)
  root = campXML.getroot()
  currentCount = campXML.find("currentCount")
  totalCount = campXML.findtext("totalCount")
  data = campXML.find("data")
  items= data.findall("item")
  #-- test
  # ET.tostring(items[0], encoding = "UTF-8").decode()

  dataset = []
  dataset = DataSet(items, year)
  return dataset
  
def DataSet(items, year):
  dataset = []

  for item in items:
    male = 0
    female = 0
    unDefine = 0
    crime = 0
    arrest = 0
    category1 = ""
    category2 = ""
    category3 = "" 
    for info in item:
      # print(info.text) #-- 데이터 값 들어 있음
        colName = info.get("name")
        if colName == "검거인원(남자)":
          male = info.text
        if colName =="검거인원(여자)":
          female = info.text
        if colName =="검거인원(불상)":
          unDefine = info.text
        if colName =="전국(발생)":
          crime = info.text
        if colName == "전국(검거)":
          arrest = info.text
        if colName == "죄종(대)":
          category1 = info.text
        if colName == "죄종(중)":
          category2 = info.text
        if colName == "죄종(소)":
          category3 = info.text

    dataset.append({
        "Male" :male,
        "Female" : female,
        "UnDefine" : unDefine,
        "Crime" : crime,
        "Arrest" : arrest,
        "Category1" : category1,
        "Category2" : category2,
        "Category3" : category3,
      })
  return dataset

