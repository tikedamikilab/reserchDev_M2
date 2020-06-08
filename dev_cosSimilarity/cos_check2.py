# tf-idfから特定問題におけるwordを抽出
# coscheck3 -> coscheck2 -> coscheck4

import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

def cos_check2(indexList, problemID, DATASET_FILE_PATH = "./datasets_output_custom3/0_tfidf_TextA2.csv"):
    dataset = pandas.read_csv(DATASET_FILE_PATH, encoding='utf-8')
    dataset = dataset[0:10000]

    with open("./datasets_output_custom3/cos_check2/cos_check2_" +str(problemID)+ ".csv", 'a',newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(dataset.columns)

    try:
        # ここで問題番号を指定．実際の問題番号とは異なるので注意 csvのindex-2
        for index in indexList:
            data_loc = dataset.loc[int(index)]

            with open("./datasets_output_custom3/cos_check2/cos_check2_" +str(problemID)+ ".csv", 'a',newline='',encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(data_loc)
    except ValueError as e:
        print('catch ValueError:', e)


if __name__ == "__main__":
    # ここで問題番号を指定．実際の問題番号とは異なるので注意 csvのindex-2
    input_datasets = pandas.read_csv("./datasets_output_custom3/0_cos_check3_0.2.csv", encoding='utf-8')
    
    for i in range(1000):
        indexList = input_datasets["cos"][i].strip('['']').split(',')
        problemID = input_datasets["problemID"][i]
        cos_check2(indexList, problemID)
