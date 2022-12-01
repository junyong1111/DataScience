# coding:utf-8

import pandas as pd
import json
import os


annoDir = "test_road_information/label/"

annoList = os.listdir(annoDir)
imgTmpDict = []
annoTmpDict = []

idNum = 1
annoIdNum = 0

for anno in annoList:
    with open(annoDir + anno, encoding="utf-8-sig", errors="ignore") as json_file:
        jsonData = json.load(json_file)
        
    
    imgPath = anno.replace(".json", ".jpg")
    imgSize = 1936 * 1464
    # print(imgPath)
    images = {
            "file_name": jsonData["image"]["filename"],
            "height": jsonData["image"]["imsize"][1],
            "width": jsonData["image"]["imsize"][0],
            "id": idNum
    }
    imgTmpDict.append(images)
    
    for i in range(len(jsonData["annotation"])):
        bbox = [
            jsonData["annotation"][i]["box"][0],
            jsonData["annotation"][i]["box"][1],
            jsonData["annotation"][i]["box"][2]-jsonData["annotation"][i]["box"][0],
            jsonData["annotation"][i]["box"][3]-jsonData["annotation"][i]["box"][1]
        ]
        # print(bbox)
        if jsonData["annotation"][i]["class"] =='traffic_sign':
            category_id = 1
        else:
            category_id = 0
        annotation = {
            "segmentation": [[]],
            "area": bbox[2]*bbox[3],
            "iscrowd": 0,
            "image_id": idNum,
            "bbox": bbox,
            "category_id": category_id,
            "id": annoIdNum,
            
        }
        annoTmpDict.append(annotation)
        annoIdNum += 1
    idNum += 1

cocoDict = {}

cocoDict["info"] = {
  "description": "소융최기 실습과제",
  "url": "https://drive.google.com/file/d/1Ap5ML2dh7oOpN50SrbTmiDgS7CxlTys1/view?usp=sharing",
  "year": 2022,
  "contributor": "Junyong",
  "date_created": "2022/11/17",
}


cocoDict["images"] = imgTmpDict
cocoDict["annotations"] = annoTmpDict

cocoDict["categories"] = [
  {"id": 0, "name": "traffic_lighjt"},
  {"id": 1, "name": "traffic_sign"},
]

with open("./2class_coco.json", 'w') as f :
    json.dump(cocoDict, f, ensure_ascii=False, indent='\t')
    print("완료했습니다.")
