import time
import os
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import cv2
from PIL import Image

import tensorflow as tf
from tensorflow import keras

# 각 클래스별 정보 확인
dir = './trafficSign/gtsrb'
    
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

from sklearn.model_selection import train_test_split

# 실습 코드 작성 🡓🡓
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