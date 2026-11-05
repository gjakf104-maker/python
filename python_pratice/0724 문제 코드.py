'''
sum = 0

for i in range(1,11):
    sum = sum + i
    
print("1부터 10까지의 합은 -> %d" %sum)

'''
##########################
'''
sum = 0  #변수 초기화
for i in range(501,1001,2):
    sum = sum + i

print("500부터 1000까지의 홀수의 합 : %d" %sum)
'''  
##############################
'''
num = int(input("값을 입력하시오 :" ))
sum = 0
for i in range(0, num+1):
    sum += i

print(" 1부터 사용자가 더한값은 -> %d" %sum)

'''

#############################
'''
sum = 0
a , b, c = 0,0,0
a = int (input("값을 입력하시오 :"))
b = int (input("값을 입력하시오 :"))
c = int (input("값을 입력하시오 :"))

for i in range(a,b,c):
    sum += i

print( "%d에서 " %sum)
'''
############################
'''
a,b = 0 ,0


a = int(input("구구단 값을 입력 :"))
b = int(input("구구단 값을 입력 :"))

num = a* b
print("원하는 구구단 값은 : %d" %num)
'''
####################################
'''
gg = int(input("원하는 값을 입력 :"))
for i in range(1,10):
    print("%d X %d = %d" %(gg, i, gg * i))
'''
#####################################
'''
i ,k = 0,0
for i in range(2,10):
    for k in range(1,10):
        print("%d X %d = %d" %(i,k,i*k))
    print (" ")

'''
#####################################
'''
num1 ,num2 = 0, 0
sum = 0
while  True: #무한 반복 구문
    num1  =  int(input("첫번째 정수 입력 :"))
    if num1 == 0:
        break 
    


    num2  =  int(input("두번째 정수 입력 :"))

    sum = num1 + num2
    print ("%d + %d= %d" %(num1,num2, sum))
'''
###############################################
i,k = 0,0
for i in range(2,10):
    print("< %d 단 >" %i)
    for k in range(1,10):
        print("%d X %d = %d" %(i , k ,i*k),end="\t")
    
