# 抽出
# 
# 並び変えるだけのやつ

import os
import sys
import time
import numpy
import pandas
import csv
import re

DATASET_FILE_PATH = "./datasets_source/python_problemA_custom.csv"
usedata=[]
with open(DATASET_FILE_PATH ,encoding="utf-8") as f:
    reader = csv.reader(f)
    for input_data in reader:
        usedata.append(input_data[0])

DATASET_FILE_PATH = "./datasets_problemText/problemText_A.csv"
with open(DATASET_FILE_PATH ,encoding="utf-8") as f:
    reader = csv.reader(f)
    for input_data in reader:
        for use in usedata:
            if input_data[0] == use:
                with open('./datasets_problemText/_custom.csv', 'a',newline='',encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(input_data)

print("fin")