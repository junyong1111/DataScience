# 자율주행 인공지능 Tensorflow 이용


# 1.교통 표지판 인식 모델 연습

실습 데이터는 German Traffic Sign Benchmark (GTSRB) 데이터셋으로 2011년 International Joint Conference on Neural Networks (IJCNN) 2011 에 개최된 대회의 데이터셋으로 39209 개의 이미지가 43 개의 클래스에 속함
폴더에 저장된 이미지와 클래스 라벨을 읽어와 직접 학습, 검증 데이터셋을 구축
사전 학습된 VGG16 모델을 활용하여 교통 표지판을 분류하는 작업에 활용

### 1. 데이터 로드와 전처리

터미널에서 다음 명령어를 사용하여 데이터를 다운로드

```bash
wget gtsrb.zip https://www.dropbox.com/s/5uc83j3aky5b9cv/gtsrb.zip
```


교통표지판 폴더를 생성 후 압축 풀기  자신의 작업환경에 맞게 설정  

- 자신의_작업환경/trafficSign/gtsrb 폴더 생성

```bash
unzip -q ./gtsrb.zip -d ./trafficSign/gtsrb
```

각 클래스별 정보 확인
```python
dir = './gtsrb'
    
plt.figure(figsize=(10, 10))
for i in range (0,43):
    plt.subplot(8,10,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    path = dir + "/Meta/{0}.png".format(i)
    img = plt.imread(path)
    plt.imshow(img)
    plt.xlabel(i)
```

모든 교통 표지판 클래스를 라벨링
```python
#dictionary to label all traffic signs class.
classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }
```

### 2.TODOS: 데이터 로드

각 클래스별 폴더에 들어가 image 파일 네임 리스트인 images 생성
images 를 for 문을 돌면서 각 이미지의 크기를 조정한 후에 image_data 리스트에 첨부하고 클래스 라벨은 image_labels 에 첨부
image_data 와 image_labels 를 numpy array로 변환

```python
NUM_CLASSES = 43
H = 64
W = 64

image_data = []
image_labels = []

# 실습 코드 작성 🡓🡓
# i는 레이블
for i in range(NUM_CLASSES):
    path = './trafficsign/gtsrb/Train/' + str(i)
    print(path)
    images = os.listdir(path)

    for img in images:
        try:
          image = cv2.imread(path + '/' + img)
          image_fromarray = Image.fromarray(image, 'RGB')
          resized_image = image_fromarray.resize((H, W))
          image_data.append(np.array(resized_image))
          image_labels.append(i)
        except:
            print("Error - Image loading")

# 리스트를 numpy array로 변환
image_data = np.array(image_data)
image_labels = np.array(image_labels)

print(image_data.shape)
#-- 이미지데이터 크기 확인
#-- (39209, 64, 64, 3)
```

### 3.TODOS: 학습, 검증 데이터셋 생성

np.random.shuffle 을 활용하여 이미지의 인덱스를 골고루 섞어줌
train_test_split 함수를 활용하여 학습/검증/시험 데이터, 학습/검증/시험험 라벨 분리, 각각 X_train/X_valid/X_test, y_train/y_valid/y_test
X_train, X_valid 를 255로 나누어 0~1 범위로 변환


```python
from sklearn.model_selection import train_test_split

# 실습 코드 작성 
# 데이터셋 셔플
shuffle_indexes = np.arange(image_data.shape[0])
np.random.shuffle(shuffle_indexes)
image_data = image_data[shuffle_indexes]
image_labels = image_labels[shuffle_indexes]

# 학습/검증/시험 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(image_data, image_labels, test_size=0.2)
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.25)

# 정규화
X_train = X_train/255.0
X_valid = X_valid/255.0
X_test = X_test/255.0
```

# 2.차선 인식 

