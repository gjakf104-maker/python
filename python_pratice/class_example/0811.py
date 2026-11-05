'''
#파이썬 + DBMS(SQLite3)

import sqlite3

#변수선언
con, cur = None, None
data1, data2, data3, data3 = "","","",""
sql = ""

# 메인 코드 부분 선언
con = sqlite3.connect("c://pythondata//sampleDB")
cur = con.cursor()

# 기존에 테이블이 만들어져 있어서 기존 테이블 사용
while(True):
    data1 = input("사용자 id 입력 -> ")
    if data1 == "":
        break
    data2 = input("사용자 이름입력 -> ")
    if data2 == "":
        break
    data3 = input("이메일 이름입력 -> ")
    if data3 == "":
        break
    data4 = input("생년월일 이름입력 -> ")
    if data4 == "":
        break
    sql = "insert into uTable values('"+ data1 +"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()
'''
'''========================================================================================='''
# 테이블에 있는 데이터 조회
import sqlite3

# 변수 선언
con, cur = None, None
data1, data2, data3, data4 = "","","",""
row = None # 행으로 자료를 조회
#메인 코드 실행 부분
con = sqlite3.connect("c://pythondata//sampleDB")
cur = con.cursor()
cur.execute("select * from uTable")
print("사용자ID 사용자 이름 이메일 출생년도")
print("====================================")

while(True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f"{data1}, {data2}, {data3}, {data4}")
''' print("%s %s %s %d " %(data1,data2,data3,data4))'''

con.close()
