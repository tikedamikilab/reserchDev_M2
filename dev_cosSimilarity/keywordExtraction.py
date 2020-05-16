# cosSimilariyEn

import os
import sys
import time
import numpy
import pandas
import csv
import re

keywordlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

DATASET_FILE_PATH = "./datasets_source/screening_python_submission4_pageA.csv"

dataset = pandas.read_csv(DATASET_FILE_PATH)
dataset = dataset[0:10000]

confidence = 0.0

# ソースコード
input_dataset = numpy.array(dataset["source"])   

for input_data in input_dataset:
    output = ""
    words = str(input_data).split()
    for word in words:
        for keyword in keywordlist:
            if word == keyword:
                output = output + " " + word

    with open('keyword.csv', 'a',newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([output])

print("fin")