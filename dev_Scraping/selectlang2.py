# 一つの言語を指定し，各問題から一人代表を抽出
# 基本codeforcesはcodesize順
# 
#######################
#language = "Python 3"
#submission = "268"
#page = "A"
#######################

import csv

def selectlang(submission, page='A',language = 'Python 3',outputfilename = 'selectlang2'):
    try:
        with open('./datasets_problemC/sample_status'+str(submission)+'_problem'+page+'.csv',encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[4] == language:
                    row.append(submission)
                    with open(outputfilename+'.csv', 'a',newline='',encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(row)
                    break
    except FileNotFoundError as e:
        print('catch KeyError:', e)

if __name__ == '__main__':
    for i in range(1000):
        selectlang(i, page='C')
    print("fin")