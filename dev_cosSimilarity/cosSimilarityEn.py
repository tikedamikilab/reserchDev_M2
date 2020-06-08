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

DATASET_FILE_PATH = "./datasets_output_custom2/0_data_problemTextA2_custom.csv"

dataset = pandas.read_csv(DATASET_FILE_PATH, encoding='utf-8')
dataset = dataset[0:10000]
# calculate tf_idf
# ソースコード
input_dataset = numpy.array(dataset['problemText'])

#設定
max_df = 0.95
min_df = 0.01
tf_idf_vectorizer = TfidfVectorizer(analyzer='word',stop_words='english', max_df = max_df, min_df = min_df)
#cipy.sparse.csr.csr_matrix型の出力
tf_idf_vector = tf_idf_vectorizer.fit_transform(input_dataset)

tf_idf_array = tf_idf_vector.toarray()

cs = cosine_similarity(tf_idf_array, tf_idf_array)

with open("./datasets_output_custom2/tfidf_.csv", 'a',newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    # tf-idf書き出し用 
    writer.writerow(tf_idf_vectorizer.get_feature_names())
    writer.writerows(tf_idf_array)

with open("./datasets_output_custom2/cos_.csv", 'a',newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    # cos類似度書き出し用
    writer.writerows(cs)

# 文書内での単語の重要度tf(term frequency)
# 一般的な単語の希少度idf(inverse document frequency)
# を掛け合わせたもの

print("fin")