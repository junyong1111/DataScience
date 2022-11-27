import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests
from urllib import parse
from XML_To_Data import ReadDataFromXML


key =  "IU%2FiwaExUBMui%2FFjciNT%2F4Md3b4RLulJyt6%2FAccAZ4V4EaVsLtIbqTn1V%2FzTBDc46%2BTlA%2B7iSEXYrzTLFrmMKw%3D%3D"
url =  "https://api.odcloud.kr/api/15064217/v1/uddi:5eb01115-6046-4320-84da-87b41ad58024"
dataPath = "/content/drive/MyDrive/Software/datasets/Kor_Police_2021_data.xml"
year = 2021
dataset = ReadDataFromXML(key,url,dataPath, year)

df = pd.DataFrame(dataset)

#-- 결측 데이터가 잇는 행 제거 열을 제거하고 싶다면 axis =1
df = df.dropna(axis=0)

#-- 데이터 합치기 이후 index 재정렬
# df = pd.concat([df1,df2,df3],axis=0)
# df = df.reset_index(drop= True)

#-- 결측 데이터 확인
df.isnull().sum()

df['Male'] = pd.to_numeric(df["Male"])
df['Female'] = pd.to_numeric(df["Female"])
df['UnDefine'] = pd.to_numeric(df["UnDefine"])
df['Crime'] = pd.to_numeric(df["Crime"])
df['Arrest'] = pd.to_numeric(df["Arrest"])
df.dtypes
#-- 정수형 데이터 변환

df1 = df.drop(["UnDefine",], axis = 1)
df1
#-- 원인 불명 삭제

df1.corr()
#-- 상관관계 확인

#-- C.f. 상관관계의 계수
#-- - x와 y가 상관관계가 있다고 하면, x가 변할 때 y가 변하는 것을 의미한다.
#-- - 얼마나 변하냐와 관련한 것이 상관관계의 계수이다.
#-- - 보통 계수가 0.2 이하이면 상관관계가 없거나 무시해도 좋은 수준
#-- - 0.4 이하는 약한 상관관계
#-- - 0.4 이상은 강한 상관관계

dfCrime =  df1.drop(["Arrest"], axis = 1)
dfCrime = dfCrime.sort_values(by='Category1' ,ascending=False)
#-- 남여 범죄 분할

dfArrest = df1.drop(["Crime"], axis = 1)
dfArrest = dfArrest.sort_values(by='Category1' ,ascending=False)
#-- 남여 검거 분할

dfCrime["CrimeRatioMan"] = dfCrime["Male"] / dfCrime["Crime"]
dfCrime["CrimeRatioWomen"] = dfCrime["Female"] / dfCrime["Crime"]
#-- 남여 범죄별 비율 

dfArrest["ArrestRatioMan"] = dfArrest["Male"] / dfArrest["Arrest"]
dfArrest["ArrestRatioWomen"] = dfArrest["Female"] / dfArrest["Arrest"]
#-- 남여 범죄별 검거 비율

dfCrime.set_index(["Category1",'Category2',"Category3"], inplace = True)
dfArrest.set_index(["Category1",'Category2',"Category3"], inplace = True)
#-- 범죄별로 정렬

dfCrime.info()