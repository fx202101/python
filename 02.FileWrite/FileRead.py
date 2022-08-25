import csv
import math

csv_file = open(r"C:\Users\qh_05\OneDrive\Code\Python\06.DBConn\hetfjp.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
cursor = conn.cursor()
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    if len(row[0])==5:
        print(row[0][0:4]+"0"+row[0][4:5])
    print(row,row[1].replace(',',''))
    # print(math.ceil(float(row[1])))
    
import datetime
tstr = '2012/2/29'
tdatetime = datetime.datetime.strptime(tstr, '%Y/%m/%d')
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdatetime.year,str(tdatetime.month).zfill(2))


