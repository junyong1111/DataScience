1. 데이터 시각화
2. 데이터 전처리
3. 데이터 분석

1. 데이터 시각화
- 숫자들의 나열보다, 흐름이나 패턴 등의 정보를 보다 쉽게 전달할 수 있다.
- 읽는 데이터를 -> 보는 데이터로 

## 시각적 속성
### 데이터 시각화
- 체계적이고 논리적인 방식
    - 데이터 값 => 시각적 속성 과정
    - 그래프(차트)를 만드는 과정

#### 그래프
- 데이터 값 => 정량화 가능한 속성으로 표현한 것

#### XML 데이터를 원하는 값만 추출
- XML_To_Data.py 파일을 이용
- 공공데이터 포털에서 원하는 API키 추출
- key
    - 공공 데이터 포털 Encoding Key입력
- url  
    - Sample OpencAPI를 이용하여 "?" 이전까지의 url 추출 
- dataPath
    - 추출한 데이터를 저장할 경로


### 데이터 처리 및 시각화

```python
import pandas as pd

#-- 판다스를 이용하여 데이터 읽기
df = pd.DataFrame(dataset)

#-- 결측 데이터가 잇는 행 제거 열을 제거하고 싶다면 axis =1
df = df.dropna(axis=0)

#-- 데이터 합치기 이후 index 재정렬
# df = pd.concat([df1,df2,df3],axis=0)
# df = df.reset_index(drop= True)

#-- 결측 데이터 확인
df.isnull().sum()

#-- 데이터 확인
df.info()

#-- 데이터 별 숫자 타입을 재정의
df['Male'] = pd.to_numeric(df["Male"])
df['Female'] = pd.to_numeric(df["Female"])
df['UnDefine'] = pd.to_numeric(df["UnDefine"])
df['Crime'] = pd.to_numeric(df["Crime"])
df['Arrest'] = pd.to_numeric(df["Arrest"])
#-- 정수형 데이터 변환


df.dtypes
#-- 데이터 타입 확인

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


#-- 남여 범죄별 비율과 범죄별 검거현황 조사를 위하여 데이터 분할

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

```

#### 시각화

```python

maleCrimeDf = dfCrime[["Male","Crime",]]
maleCrimeDf
maleCrimeDf.sort_values(
  by='Crime', ascending=True).plot(kind="barh", logx=True)
plt.xlabel("남성 강력범죄 수")
plt.legend(loc='lower right')
plt.show()

#-- 일어난 범죄 중 남성이 저지른 횟수

# print(maleDF.index)
label = maleCrimeDf.loc[('강력범죄','살인(기수)' )]
#-- 강력범죄, 살인(기수)로 분할
label = label.reset_index()
labels = label["Category3"].value_counts().index.tolist()
labels
male = label["Male"]
fracs1 =  male.values
fracs1
explode = (0.25,0,0,0,0,0)

plt.pie(fracs1,explode = explode,
        labels = labels, autopct ="%0.0f%%",shadow =True,
        )
plt.title("남성 강력범죄(살인) 중 가장 많은 범죄는 살인")
plt.show()

maleCrimeRatioDf = dfCrime[["CrimeRatioMan",]]
maleCrimeRatioDf
maleCrimeRatioDf.sort_values(
  by='CrimeRatioMan', ascending=True).plot(kind="barh", )
plt.xlabel("남성 강력범죄 수")
plt.legend(loc='lower right')
plt.show()

#-- 일어난 범죄 중 남성이 저지른 횟수


# print(maleDF.index)
label = maleCrimeDf.loc[('강력범죄','살인(기수)' )]
#-- 강력범죄, 살인(기수)로 분할
label = label.reset_index()
labels = label["Category3"].value_counts().index.tolist()
labels
male = label["Male"]
fracs1 =  male.values
fracs1
explode = (0.25,0,0,0,0,0)

plt.pie(fracs1,explode = explode,
        labels = labels, autopct ="%0.0f%%",shadow =True,
        )
plt.title("남성 강력범죄(살인) 중 가장 많은 범죄는 살인")
plt.show()

maleCrimeRatioDf = dfCrime[["CrimeRatioMan",]]
maleCrimeRatioDf
maleCrimeRatioDf.sort_values(
  by='CrimeRatioMan', ascending=True).plot(kind="barh", )
plt.xlabel("남성 강력범죄 수")
plt.legend(loc='lower right')
plt.show()

#-- 일어난 범죄 중 남성이 저지른 횟수


# print(maleDF.index)
label = maleCrimeDf.loc[('강력범죄','살인(미수등)' )]
#-- 강력범죄, 살인(기수)로 분할
label = label.reset_index()
labels = label["Category3"].value_counts().index.tolist()
labels
male = label["Male"]
fracs1 =  male.values
fracs1
explode = (0.25,0,0,0)

plt.pie(fracs1,explode = explode,
        labels = labels, autopct ="%0.0f%%",shadow =True,
        )
plt.title("남성 강력범죄(미수) 중 가장 많은 범죄는 살인")
plt.show()

femaleCrimeDf = dfCrime[["Female","Crime",]]
# maleDF
femaleCrimeDf.sort_values(
  by='Crime', ascending=True).plot(kind="barh", logx=True)
plt.xlabel("여성 강력범죄 수")
plt.legend(loc='lower right')
plt.show()
#-- 일어난 범죄 중 여성이 저지른 횟수

# print(maleDF.index)
label = femaleCrimeDf.loc[('강력범죄','살인(기수)' )]
#-- 강력범죄, 살인(기수)로 분할
label = label.reset_index()
labels = label["Category3"].value_counts().index.tolist()
male = label["Female"]
fracs1 =  male.values
explode = (0.25,0,0,0,0,0)

plt.pie(fracs1,explode = explode,
        labels = labels, autopct ="%0.0f%%",shadow =True,
        )
plt.title("여성 강력범죄 중 가장 많은 범죄는 살인")
plt.show()

# print(maleDF.index)
label = femaleCrimeDf.loc[('강력범죄','살인(미수등)' )]
#-- 강력범죄, 살인(기수)로 분할
label = label.reset_index()
labels = label["Category3"].value_counts().index.tolist()
male = label["Female"]
fracs1 =  male.values
explode = (0.25,0,0,0)

plt.pie(fracs1,explode = explode,
        labels = labels, autopct ="%0.0f%%",shadow =True,
        )
plt.title("여성 강력범죄(미수) 중 가장 많은 범죄는 살인")
plt.show()

femaleCrimeRatioDf = dfCrime[["CrimeRatioWomen",]]
femaleCrimeRatioDf
femaleCrimeRatioDf.sort_values(
  by='CrimeRatioWomen', ascending=True).plot(kind="barh", )
plt.xlabel("여성 강력범죄 수")
plt.legend(loc='lower right')
plt.show()

#-- 일어난 범죄 중 여성이 저지른 횟수

Arrest = df1.drop(["Male","Female"], axis = 1)
Arrest = Arrest.sort_values(by='Category1' ,ascending=False)
Arrest.set_index(["Category1",'Category2',"Category3"], inplace = True)
ArrestDf = Arrest[["Arrest","Crime",]]
# ArrestDf

ArrestDf.sort_values(
  by='Crime', ascending=True).plot(kind="barh", logx=True,)
plt.xlabel("범죄 별 검거 현황")
plt.legend(loc='lower right')

plt.show()


```