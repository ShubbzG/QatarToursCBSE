import pandas as pd
import mysql.connector

def backup():
    conn = mysql.connector.connect(host='localhost',database='QATARTRAVELS',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from TOURS")
    ls = pd.DataFrame(cursor.fetchall())
    ls.to_csv('tours.csv')
    cursor.execute("select * from members")
    ls = pd.DataFrame(cursor.fetchall())
    ls.to_csv('members.csv')
    
backup()
