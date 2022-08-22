import pyodbc
import csv
import datetime
import math
# 数据库文件  
DBfile = r"D:\onedrive\Code\Python\06.DBConn\db.accdb" 

# conn = pyodbc.connect(u"Driver={Driver do Microsoft Access (*.mdb,*.accdb)};DBQ=" + DBfile)
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=D:\onedrive\Code\Python\06.DBConn\db.accdb;'
    )
conn = pyodbc.connect(conn_str)

csv_file = open(r"D:\onedrive\Code\Python\02.FileWrite\HS.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
cursor = conn.cursor()
for row in f:
    sdate=datetime.datetime.strptime(row[0], '%Y/%m/%d')
    #create exec sql
    SQL = "insert into stockHistory(sdate,sid,sname,hight,low,open,close) values('"
    SQL =SQL + str(sdate.year)+str(sdate.month).zfill(2)+"',"
    SQL =SQL+"'1001','HETFCN',"+str(math.ceil(float(row[2])))+","+str(math.ceil(float(row[3])))+","+str(math.ceil(float(row[1])))+","+str(math.ceil(float(row[4])))+")"
    print(SQL)
    cursor.execute(SQL)
    cursor.commit()

cursor.close()
conn.close()
