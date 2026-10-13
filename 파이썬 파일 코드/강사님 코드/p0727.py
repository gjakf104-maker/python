'''
# 변수 선언(단수 데이터) 
a, b, c, d = 0, 0, 0, 0
sum = 0

a = int(input("첫번째 정수 입력 : "))
b = int(input("두번째 정수 입력 : "))
c = int(input("세번째 정수 입력 : "))
d = int(input("네번째 정수 입력 : "))

sum = a + b + c + d;

print("합은 -> %d" % sum)


list = [0,0,0,0] # 복수 데이터 
sum = 0
for i in range(0, 4):   
    list[i] = int(input("%d번째정수 : " % (i + 1)))

for i in range(0, 4):
    sum = sum + list[i]

print("합은 -> %d" % sum)



list = []

for i in range(0, 4):
    list.append(0)

sum = 0

for i in range(0, 4):
    list[i] = int(input(str(i + 1) + "번째 숫자 : "))

for i in range(0, 4):
    sum = sum + list[i]

print("합은 -> %d" % sum)

'''

# 리스트 조작 함수
myList = [30,10,20]
print("현재 리스트는 -> %s" % myList)

myList.append(40)
print("append() 후의 리스트는 -> %s" % myList)

print("pop() 에 의해 추출된 값은 -> %s" % myList.pop())
print("pop() 함수 사용한 후의 리스트는 -> %s" % myList)

myList.sort()
print("sort() 함수 사용한 후의 리스트 -> %s" % myList)

myList.reverse()
print("reverse() 함수 사용후의 리스트 -> %s" % myList)

print("데이터 값 20의 위치는 -> %d" % myList.index(20))

myList.insert(2, 60)
print("insert() 함수를 사용한 후의 리스트 -> %s" % myList)

myList.remove(60)
print("remove() 함수를 사용한 후의 리스트 -> %s" % myList)

print("myList에서 데이터 값 30의 개수는 -> %d" % myList.count(30))












