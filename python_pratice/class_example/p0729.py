'''
# 함수 선언
def func1():
    result = 100
    return result

def func2():
    print("반환값을 가지고 있지 않은 함수")
    
# 전역 변수 선언
sum = 0

# 메인 코드 작성
sum = func1()
print("func1() 함수에서 돌려준 값은 -> %d" % sum)
func2()


#함수 선언
def func1(*para):
    result = 0

    count = len(para)
    for num in para:
        result = result + num

    return result

#전역 변수
sum = 0
count = 0

#메인 부분
sum = func1(10, 20, 30)
print("%d개 입력한 결과 값은 -> %d" % (count, sum))

sum = func1(10, 20, 30, 40, 50, 60)
print("출력한 결과 값은 -> %d" % sum)


str = "Python"

cnt = len(str)

for i in range(0, cnt):
     print(str[i] + '^', end = '')
     
'''

str = input("문자열 입력 : ")
cnt, i = 0, 0 # cnt : 입력한 문자열의 길이값 담을 변수
str1 = ""
cnt = len(str)

for i in range(0, cnt):
    str1 = str1 + str[cnt - (i + 1)]

print("역으로 출력한 문자 -> %s" % str1)















