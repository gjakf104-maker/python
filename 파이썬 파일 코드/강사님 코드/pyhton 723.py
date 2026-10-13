'''
a = 100

if a < 50 :
    print("50보다 작군요")
    print("이문장은 과역 출력이 ?")

print("프로그램 종료")
'''
#----------------------------------------------------------

# 사용자가 정수를 입력해서 입력한 정수가 짝수, 홀수 인지 검사
'''
num  = int(input("숫자를 입력해주세요 :"))

if num % 2 == 0:
    print("짝수를 입력해군요")
else:
    print("홀수를 입력해군요")
'''

#학점 프로그램( 다중 if구문)

#점수 입력(변수선언)
'''
score = int(input("점수를 입력 :"))

if score >= 90:
    print("A학점")

else:
    if score >= 80 :
        print("B학점")
    else :
        if score >= 70:
            print("C학점")
        else :
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")
'''
#간단한 코드 else if ----> elif
'''
score = int(input("점수를 입력 :"))

if score >= 90:
    print("A학점")

elif score >= 80 :
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")

--------------------------------------------------
score = 57
result = ''  #문자열을 담는 변수

if score >= 60 :
    result = '합격'
else :
    result = '불학격'

print(result)
#---------------------------------

#파이썬의 삼항 연산자 (삼항에서는 result는 변수는 하나만 선언해도 가짐)
score = 60
result = '합격'  if score >= 60  else '불합격'
print(result)
'''
#--------------------------------------
name = input("이름을 입력하세요")

if name == 황재필 :
    print("개씨발쌔끼")


    
 

'''

print("처음으로 for구문을 사용해서 출력" *3)
print("처음으로 for구문을 사용해서 출력" *3)
print("처음으로 for구문을 사용해서 출력" *3)



for i in range(0,10):
    print("처음으로 for구문을 사용해서 출력")
'''
