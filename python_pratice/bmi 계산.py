import sqlite3
con, cur = None, None
data1, data2 ,data3, data4 ="","","",""
res = ""

con = sqlite3.connect("c://pythondata//sampleDB2")
cur = con.cursor()
'''cur.execute("create table Ctable(tall,weight,foot size, bmi)")'''

while(True):
    data1 = input("키를 입력하시오(소숫점으로 입력) :")
    if data1 == "":
        break
    data2 = input("몸무게를 입력하시오 :")
    if data2 == "":
        break
    data3 = input("발사이즈를 입력하시오 :")
    break
    
data4= int(float(data2)/float(data1)**2)
print(f"bmi는 {data4}입니다")

res = "insert into Ctable values('+data1+','+data2+','+data3+','+data4+')"
cur.execute(res)

con.commit()
con.close()

