#  변수선언(단수 데이터)
'''
a, b, c, d = 0,0,0,0
sum = 0
a = int(input("첫번째 정수 입력"))
b = int(input("두번째 정수 입력"))
c = int(input("세번째 정수 입력"))
d = int(input("네번째 정수 입력"))

sum = a+b+c+d
print("합--> %d" %sum)
'''
############################################################

'''
list = [0,0,0,0] #복수 데이터 
sum = 0

list[0] = int(input("1번째 정수 입력"))
list[1] = int(input("2번째 정수 입력"))
list[2] = int(input("3번째 정수 입력"))
list[3] = int(input("4번째 정수 입력"))

sum = list[0]+ list[1] + list [2] + list[3]

print("합 --> %d" %sum)
'''
##############################################################
'''
list = [0,0,0,0] #복수 데이터 
sum = 0

for s in [0,1,2,3]
list[s] = int(int("f{s}번째 정수 입력:"))


sum = list[s] + list[s]'''
################################################################
'''
list = [0,0,0,0] #복수 데이터 
sum = 0
for i in range(0,4):
    list[i] = int(input("%d번째 정수 입력" %(i+1)))

for i in range(0,4):
    sum = sum + list[i]


print("합 --> %d" %sum)
'''
#####################################################################
'''
list = []
for i in range(0,4):
    list.append(0)

sum = 0

for i in range(0,4):
    list[i] = int(input(str(i+1) + "번째 숫자 :"))

for i in range(0,4):
    sum = sum + list[i]
print("합 --> %d" %sum)

'''

#리스트 조작 함수
myList = [30,10,20]
print("현재 리스트는 -> %s" %myList)

myList.append(40)
print("append()후의 리스트는-> %s " %myList)
#pop()은 배열 맨 마지막을 제거
print("pop() 에 의해 추출된 값은 -> %s" %myList.pop())
print('pop()에 의해 추출된 리스트는 -> %s ' %myList)

myList.sort()   #sort는 오름차순는 리스트 값이 바꿔버림 # sorted는 보여줄때만
print("sort() 함수 사용한 후 --> %s" %myList)

myList.reverse()
print("reverse() 함수 --> %s" %myList)

print("데이터 값 20의 위치 -> %d" %myList.index(20))

myList.insert(2,60)
print("insert() 함수를 사용한 후의 리스트 -> %s" %myList)

myList.remove(60)
print("remove() 함수를 사용한 후의 리스트 -> %s" %myList)

print ("myList에서 데이터 값 30의 개수는 -> %d" %myList.count(30))
