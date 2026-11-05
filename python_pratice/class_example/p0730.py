'''
numberInput = "   Python   Program   "
result = ""

for i in range(0, len(numberInput)):
    if numberInput[i] != ' ':
        result = result + numberInput[i]

print("원본 문자열 -> " + '[' + numberInput + ']')
print("공백 제거한 문자열 -> " + '[' + result + ']')


# 문자열을 입력 받는 변수
str = input("문자열을 입력 : ")

print("결과 문자열 출력 -> ", end = '')
for i in range(0, len(str)):
    if str[i] != 'r':
        print(str[i], end = '')
    else:
        print('^', end = '')
        


str = input("문자열을 입력 : ")

print("결과 문자열 출력 -> ", end = '')

print(str.replace('r', '^'))

'''

from tkinter import *

window = Tk()
window.title("윈도우 창")
window.mainloop() 








      

