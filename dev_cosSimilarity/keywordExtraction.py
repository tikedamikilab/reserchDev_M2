# keyword 抽出
# 
# id,day,author,problem,language,ac,len,word,source,token,time,memory,status
# DATASET_FILE_PATH = "./datasets_source/screening_python_submission4_pageA.csv"

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

DATASET_FILE_PATH = "./datasets_source/python_problemC.csv"

with open(DATASET_FILE_PATH ,encoding="utf-8") as f:
    reader = csv.reader(f)
    for input_data in reader:
        output = ""
        words = str(input_data[8]).split()
        for word in words:
            for keyword in keywordlist:
                if word == keyword:
                    output = output + " " + word
        if output == "":
            continue
        else:
            with open('keyword.csv', 'a',newline='',encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([input_data[12], output])

print("fin")