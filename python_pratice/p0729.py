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
print("func1() 함수에서 돌려준 값은 -> %d " %sum)
func2()


# 함수 선언
def mul(v1, v2):
     result = []   #리스트 선언
     res1 = v1 + v2
     res2 = v1 -  v2
     result.append(res1)
     result.append(res2)
     return  result

# 전역 변수 선언
myList = [] #리스트 선언(공백)
sum, sub = 0, 0

# 메인 부분
myList = mul(100,200) 
sum = myList[0]
sub =myList[1]

print(f" mul()함수에서 받은 값은  {sum}, {sub}")


def cal(v1,v2):
    result = []
    res1 = v1 ** v2
    res2 = v1/ v2
    result.append(res1)
    result.append(res2)
    return result

List = []
List = cal(2,3)
print(List[0])

# 함수 선언
def osm1(*para):
    result = 0
    global cnt
    cnt = len(para)
    for num in para:
        result += num
    return result

#전역 변수
sum = 0
cnt = 0
#메인 부분
sum = osm1(10,20,30,40,50)


print(f"{cnt}개의 합 : {sum}")


str = "python"
cnt = len(str)
for i  in range(0, cnt):
    print(str[i] + '^', end = '')
          


str = input("문자열을 입력하세요 :")
rev= str[::-1]
print(f"입력한 문자열을 역으로 출력한 결과 : {rev}")
'''
'''
str = input("문자열을 입력하세요 :")
snt = len(str)
for i in range(snt,-1):
    print("str[i]" , end ='')
'''

str = input("문자열 입력 :")
cnt, i = 0,0
str1 = ""
cnt = len(str)

for i in range(0,cnt):
    str1 = str1 + str[cnt-(i+1)]

print("%s" %str1)








