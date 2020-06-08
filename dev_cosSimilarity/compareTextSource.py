# cosSimilariyEn

import os
import sys
import time
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

DATASET_PROBLEM_PATH = "./datasets_output_custom/cos_TextA_custom.csv"
DATASET_SOURCE_PATH = "./datasets_output_custom/cos_sourceA_custom.csv"
problem = pandas.read_csv(DATASET_PROBLEM_PATH, header=None, encoding='utf-8')
source = pandas.read_csv(DATASET_SOURCE_PATH, header=None, encoding='utf-8')

problem_confidence = 0.3
source_confidence = 0.4

problem_realmean = problem.mean()
source_realmean = source.mean()

# problem_temp=problem.where(problem > problem_confidence, -1)
# problem_normal = problem_temp.where(problem_temp <= problem_confidence, 1)

# source_temp = source.where(source > source_confidence, -1)
# source_normal = source_temp.where(source_temp <= source_confidence, 1)

# output = problem_normal * source_normal

# problem_mean = problem_normal.mean()
# source_mean = source_normal.mean()
# output_mean = output.mean()

# problem_allmean = problem_mean.mean()
# source_allmean = source_mean.mean()
# output_allmean = output_mean.mean()

print(problem_realmean.var)
print(source_realmean.var)
# print(output_allmean)

# source_realmean.to_csv('datasets_output_custom/source.csv', mode='x', header=False, index=False)
# problem_realmean.to_csv('datasets_output_custom/Text.csv', mode='x', header=False, index=False)
# output_mean.to_csv('datasets_output_custom/product.csv', mode='x', header=False, index=False)


print("fin")