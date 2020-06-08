# coscheck2で使うリストを作成するためのもの
# coscheck3 -> coscheck2 -> coscheck4


import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

def cos_check3(targetProblem):
    DATASET_FILE_PATH = "./datasets_output_custom2/cos_TextA2_index.csv"

    dataset = pandas.read_csv(DATASET_FILE_PATH, encoding='utf-8')
    dataset = dataset[0:10000]

    output = []
    try:
        for i in range(len(dataset)):
            if dataset[str(targetProblem)][i] > 0.2:
                output.append(i)

        with open("./datasets_output_custom3/cos_check3.csv", 'a',newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([targetProblem, output])
    except KeyError as e:
        print('catch KeyError:', e)

if __name__ == "__main__":
    for i in range(0, 1000):
        cos_check3(i)
