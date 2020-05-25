# cosSimilariyEn

import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

# This dataset comes from the UCI Machine Learning Repository.
# Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
# https://www.kaggle.com/uciml/news-aggregator-dataset
#DATASET_FILE_PATH = "./datasets/uci-news-aggregator.csv"
#RESULT_FILE_PATH = "./output/similarity_calc_result.csv"

# DATASET_FILE_PATH = "./datasets_source/python_testdata6.csv"
# DATASET_FILE_PATH = "./datasets_source/screening_python_submission1348_pageA.csv"
DATASET_FILE_PATH = "./datasets_source/python_problemA.csv"

dataset = pandas.read_csv(DATASET_FILE_PATH)
dataset = dataset[0:10000]

confidence = 0.0

# calculate tf_idf
# ソースコード
input_dataset = numpy.array(dataset["source"])
#設定
tf_idf_vectorizer = TfidfVectorizer(analyzer="word", ngram_range=(1, 1), min_df=1, stop_words="english")
#cipy.sparse.csr.csr_matrix型の出力
tf_idf_vector = tf_idf_vectorizer.fit_transform(input_dataset)

tf_idf_array = tf_idf_vector.toarray()

# cs = cosine_similarity(tf_idf_array, tf_idf_array)

with open("./dataset_output/tfidf.csv", 'a',newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # cos類似度書き出し用
    # writer.writerows(cs)

    # tf-idf書き出し用 
    writer.writerow(tf_idf_vectorizer.get_feature_names())
    writer.writerows(tf_idf_array)

# 文書内での単語の重要度tf(term frequency)
# 一般的な単語の希少度idf(inverse document frequency)
# を掛け合わせたもの

print("fin")