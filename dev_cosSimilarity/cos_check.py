# 特定のワードが使われている問題を抽出

import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

DATASET_FILE_PATH = "./datasets_output_custom2/tfidf_TextA2.csv"

dataset = pandas.read_csv(DATASET_FILE_PATH, encoding='utf-8')
dataset = dataset[0:10000]

word = 'square'

for i in range(len(dataset)):
    if dataset[word][i] != 0:
        print(dataset['problemID'][i])

# with open("./datasets_output_custom2/cos_check.csv", 'a',newline='',encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerows()

print("fin")