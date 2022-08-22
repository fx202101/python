import csv
import math

csv_file = open(r"D:\onedrive\Code\Python\02.FileWrite\HS.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    print(row)
    print(math.ceil(float(row[1])))
    
import datetime
tstr = '2012/2/29'
tdatetime = datetime.datetime.strptime(tstr, '%Y/%m/%d')
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdatetime.year,str(tdatetime.month).zfill(2))