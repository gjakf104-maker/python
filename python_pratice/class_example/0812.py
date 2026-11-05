'''import random #모듈 사용
dom = random.randint(1,100)
count = 0
ran = 0
while True:
    ran = int(input("숫자를 입력해주세요 :"))
    count += 1
    if ran > dom:
        print("너무 높은 숫자입니다")
    elif ran < dom:
        print("너무 낮은 숫자 입니다")
    else:
        print(f"정답입니다. 총 시도 횟수:{count}")
        break 
'''
import random
tries = 0 #시도 횟수를 담을 변수
guess = 0 #사용자가 입력하는 변수

# 1부터 100사이의 정수 값 선택
com_number = random.randint(1,100)

print("1부터 100사이의 숫자를 맞혀주세요")

while guess != com_number:
    guess = int(input("\n숫자를 입력하세요"))
    tries += 1
    if guess < com_number:
        print("너무 낮은 숫자입니다")
    elif guess > com_number:
        print("너무 높은 숫자입니다")

if guess == com_number:
    print(f"정답입니다. 시도 횟수 = {tries}")
else:
    print(f"정답은 {com_number}")
