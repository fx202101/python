import pyodbc
import csv
import datetime
import math

# conn = pyodbc.connect(u"Driver={Driver do Microsoft Access (*.mdb,*.accdb)};DBQ=" + DBfile)
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\qh_05\OneDrive\Code\Python\06.DBConn\db.accdb;'
    )
conn = pyodbc.connect(conn_str)

csv_file = open(r"C:\Users\qh_05\OneDrive\Code\Python\06.DBConn\hetfjp.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
cursor = conn.cursor()
for row in f:
    if len(row[0])==5:
        sdate=row[0][0:4]+"0"+row[0][4:5]
    else:
        sdate=row[0]
    #create exec sql
    SQL = "insert into stockHistory(sdate,sid,sname,hight,low,open,close) values('"
    SQL =SQL + sdate +"',"
    SQL =SQL+"'1002','HETFJP',"+row[2].replace(',','')+","+row[3].replace(',','')+","+row[1].replace(',','')+","+row[4].replace(',','')+")"
    print(SQL)
    cursor.execute(SQL)
    cursor.commit()

cursor.close()
conn.close()
