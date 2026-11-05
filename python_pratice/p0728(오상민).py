''''
myList = [30,10,20]
newList = sorted(myList)
print("sorted() 사용한 후의 myLsit -> %s" %myList)
print("sorted() 사용한 후의 newLsit -> %s" %newList)


myTuple = (10,20,30)
myList = list(myTuple) # 튜플을 리스트로 변경
myList.append(40) #[10,20,30,40]
myTuple = tuple(myList)
print(myTuple)
'''
'''
def calc(v1, v2):
    result = 0
    result = v1 + v2
    return result

sum = 0 #전역 변수

# 이 프로그램을 실행할 메인 부분
sum = calc(100,20)
print(f"100과 20의 합은 -> {sum}")
'''
'''
# 함수선언(연산 프로그램)

def calc(v1,v2,op):
    result = 0

    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        result = v1 / v2

    return result

# 전역변수 선언
res = 0
var1, var2, oper = 0, 0, " "

#메인 코드 부분
oper = input("원하는 연사자를 입력(+ - / *) :")
var1 = int(input(" 첫번쨰 정수 입력 : "))
var2 = int(input(" 첫번쨰 정수 입력 : "))

res = calc(var1, var2, oper)
print(f"{var1} {oper} {var2} = {res}")


def func1():
    a = 10 #지역변수
    print("func1() 함수에서 a의 값은 -> %d" %a)

def func2():
    print("func2() 함수에서 a의 값은 -> %d" %a)

a = 20 # 전역변수 
func1()
func2()
'''
############################################################

def func1():
    global a  #함수안의 변수를 전역변수로 눈속임, a변수는  func1() 함수안에서는 전역변수가된다.`
    a = 10 #지역변수, global 선언시 전연변수보다 지역변수가 우선권을 가짐
    print("func1() 함수에서 a의 값은 -> %d" %a)

def func2():
    print("func2() 함수에서 a의 값은 -> %d" %a)

a = 20 # 전역변수 

func1()
func2()











