# tfidfから頻出ワードを抽出
# coscheck3 -> coscheck2 -> coscheck4

import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

def cos_check4(index):
    DATASET_FILE_PATH = "./datasets_output_custom3/cos_check2/cos_check2_" + str(index) + ".csv"

    # 閾値
    threshold1 = 0.8
    threshold2 = 0.6
    threshold3 = 0.4


    dataset = pandas.read_csv(DATASET_FILE_PATH, encoding='utf-8')
    dataset = dataset[0:10000]

    output1 = []
    output2 = []
    output3 = []

    for column in dataset.columns:
        column_cnt = 0
        for data in dataset[column]:
            if data != 0:
                column_cnt += 1
        if column_cnt / len(dataset) > threshold1:
            output1.append(column)
        if column_cnt / len(dataset) > threshold2:
            output2.append(column)
        if column_cnt / len(dataset) > threshold3:
            output3.append(column)

    with open("./datasets_output_custom3/cos_check2/cos_check4.csv", 'a',newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([str(index), output1, output2, output3])

if __name__ == "__main__":
    cos_check4(1)
