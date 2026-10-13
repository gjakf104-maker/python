#1번 문제
'''
n = 0
for n in range(1,11):
    if n % 2 ==0:
        print(" 짝 -> %d" %n)
 
'''
#2번 문제
'''
sc = [85, 60, 92, 45 ,78 ,100]

for score in sc:
    if score > 70:
        print("%d : 합격입니다" %score)
    else:
        print("%d : 불합격입니다" %score)
'''
#1번 문제
'''
num = [10, -5, 3, -8, 0, -1, 7]
for number in num:
    if number<0:
        print(f" {number}는 음수")
    
'''  
'''
#2번 문제
num = 0
for num in range(1,21):
    if num%3 == 0:
        print(f"{num}")
'''

#3번 문제
'''    
fru = ["사과", "바나나", "감", "복숭아", "수박", "파인애플"]
for fruit in fru:
    if len(fruit)>= 4:
        print(f" {fruit}")
        '''
#4번 문제
'''
A,B = 0,0
A = int(input("구매 물건 값 :"))
B = int(input("두 번째 구매 물건 값 :"))
if (A+B)>50_000:
    print("무료 배송 대상입니다")
else :
    print("배송비는 3000원 입니다>")
'''

#5번 문제
'''
for w in range(1,6):
    if w%2==0:
        print(f"{w}번 손님, A구역으로 입장하세요")
        
    else :
        print(f"{w}번 손님, B구역으로 입장하세요")
'''
