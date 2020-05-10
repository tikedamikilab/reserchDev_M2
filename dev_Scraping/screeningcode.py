# scraping4.pyの実行結果から重複したコードを削除する
#
import csv

#######################
language = "Python 3"
submission = "1348"
page = "A"
#######################

source = []
with open('./datasets_source/python_source_submission' + submission +'_page'+page+'.csv', 'r' ,encoding="utf-8") as f:
    reader = csv.reader(f)    
    for row in reader:
        if row[4] == language:
            if row[8] in source:
                continue
            else:
                source.append(row[8])
                with open('screening_python_submission' + submission +'_page'+page+'.csv', 'a',newline='',encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
