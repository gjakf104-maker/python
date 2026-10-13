'''
numberInput = "    Pyhton   Program   "
result =""

for i in range(0, len(numberInput):
               if numberInput[i] != " ":
               result = result + numberInput[i]


print("원본 문자열 -> " + '['numberInput + ']')
print("공백  제거한 문자열 ->" + '[' +result +']')
               
----------------------------------------------------------------
str,A,B = '','',''
str = input("문자열을 입력 :")
A = input("바꾸고 싶은 문자를 입력: ")
B = input("바꾸고 싶은 문자를 입력: ")
for i in str(0,len(str)):
    result = result + str[i]

    if A == str[i] :
        del str[i]
        insert(B, str[i])
        result = result + str[i]
        # str에 b를 대입코드작성
        
print("result")

---------------------------------------------------------------
str = input("문자열을 입력 :")
print ("결과 문자열을 출력 -> ", end ='')
for i in range(0, len(str)):
    if  str[i] != 'r':
        print(str[i] ,end ='')
    else:
            print('^', end ='')
--------------------------------------------------
str = input("문자열을 입력 :")
print ("결과 문자열을 출력 -> ", end ='')
print(str.replace('r','^'))
---------------------------------------------------
str = "Python 언어는 아주 쉽다"
str.split()
'''

# 그래픽노드 모듈
from tkinter import *

window = Tk()
window.mainloop()

