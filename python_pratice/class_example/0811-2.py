'''str = "파이썬 언어는 쉽다. 그러므로 파이썬을 매일 매일 공부하고 싶다."
strList = []
index = 0
while True:
    try:
        index = str.index('파이썬', index)
        strList.append(index)
        index = index + 1
    except:
        break

print("파이썬 글자위치 ->" ,strList)
'''


num1 = input("숫자1 ->")
num2 = input("숫자2 ->")

try:
    num1 =int(num1)
    num2 =int(num2)
    while True:
        result = num1/num2
        
    

except ValueError:
        print("문자열은 숫자로 변환불가")

except ZeroDivisionError:
        print("0으로는 나눌 수 없다.")

except KeyboardInterrupt:
        print("잘못 누름")
