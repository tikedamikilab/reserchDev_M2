import csv

#######################
language = "Python 3"
submission = "4"
page = "A"
#######################

with open('./datasets/sample_status'+submission+'_problem'+page+'.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[4] == language:
            with open('python_status' + submission +'_problem'+page+'.csv', 'a',newline='',encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(row)
