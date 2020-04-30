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

DATASET_FILE_PATH = "./datasets/pythonTop2.csv"
RESULT_FILE_PATH = "./output/cossimilarity_sample.csv"

dataset = pandas.read_csv(DATASET_FILE_PATH)
dataset = dataset[0:10000]

confidence = 0.0

# calculate tf_idf
# ソースコード
input_dataset = numpy.array(dataset["token"])
#設定
tf_idf_vectorizer = TfidfVectorizer(analyzer="word", ngram_range=(1, 3), min_df=1, stop_words="english")
#cipy.sparse.csr.csr_matrix型の出力
tf_idf_vector = tf_idf_vectorizer.fit_transform(input_dataset)

tf_idf_array = tf_idf_vector.toarray()

cs = cosine_similarity(tf_idf_array, tf_idf_array)

with open("./output/tmp.csv", 'a',newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(cs)
    # writer.writerow(tf_idf_vectorizer.get_feature_names())
    # writer.writerows(tf_idf_array)

# 文書内での単語の重要度tf(term frequency)
# 一般的な単語の希少度idf(inverse document frequency)
# を掛け合わせたもの

# 別の方法を試すので一旦停止
# calculate similaritis
# similarities_calc_result = []
# # TD_IDF vector Iteration
# for item_index, item in enumerate(tf_idf_vector):
#     # calculate cosine similarities
#     similarities = cosine_similarity(item, tf_idf_vector)

#     # sort in ascending order
#     similarities_index = similarities.argsort()[0][-2:-12:-1]

#     # cocine similarities Iteration
#     for sim_index in similarities_index:
#         similarity = similarities[0][sim_index]

#         # if similarity is higher than confidence, save it to result object
#         if similarity > confidence and similarity < 1:
#             similarities_calc_result.append([int(item_index), int(dataset["id"][sim_index]), similarity])
#             # show progress
#             # print("progress:", item_index/len(dataset.index))

# # save result as csv format
# result = pandas.DataFrame(similarities_calc_result, columns=["Source_ID", "Similar_ID", "Similarity"])
# result.to_csv(RESULT_FILE_PATH, index=False)

print("fin")

# predict similar news with input id
# print("please input which news_id you like...")
# input_id = int(input())
# sim_id = 0

# print("you selected below news:")
# print(dataset.loc[[input_id], ["source"]])
# print("######################################")
# print("Below are similar news:")
# for result_index, sim_id in enumerate(result.ix[result["Source_ID"] == input_id]["Similar_ID"]):
#     print(sim_id, ":", dataset.loc[sim_id]["source"])

# if (len(result.ix[result["Source_ID"] == input_id]["Similar_ID"]) == 0):
#     print("Nothing to show.")