# 抽出
# 
# ソースコードがある問題文を抽出

import os
import sys
import time
import numpy
import pandas
import csv
import re

DATASET_FILE_PATH = "./datasets_source/python_problemA_custom.csv"

with open(DATASET_FILE_PATH ,encoding="utf-8") as f:
    reader = csv.reader(f)
    for input_data in reader:
        with open('./datasets_problemText/problemTextA_custom.csv', 'a',newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([input_data[12], input_data[3],input_data[8]])

print("fin")