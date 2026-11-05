'''
f = open("c://pythondata//data1.txt","w")
for i in range(1,11):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)


f.close()

------------------------------------------------------
f = open("c://pythondata//data1.txt","r")
while True:  #무한 반복 구문
    line = f.readline()
    if not line: # 더 이상 읽을 라인이 없으면
        break #강제 종료
    print(line)
f.close()
-------------------------------------------------------

f = open("c://pythondata//data1.txt","r")
lines = f.readlines()
for line in lines:
    print(line)

f.close()


f = open("c://pythondata//data1.txt" ,"r")
d = f.read()
print(d)
f.close()


f = open("c://pythondata//data1.txt","a")
for i in range(21,31):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)


f.close()

f = open("c://pythondata//data2.txt","w")
f.write("Python is programming")
f.close()


with open("c://pythondata//data3.txt","w") as f:
    f. write("java program")
'''
f = open("c://pythondata//data2.txt","r")
d = f.read()
print(d)
