#변수선언 시 초기화           초기값
money. c500, c100, c50, c10 = 0, 0, 0, 0, 0 ;

#메인 코드 작성
money = int(input("교환할 돈을 입력: "))


c500 = money // 500
money &=500

c100 = money //100
money %= 100

c50 = money //50
money %= 50

c10 = money //10
money %= 10

print("500원 짜리 동전 -> %d개" % c500)
print("100원 짜리 동전 -> %d개" % c100)
print("50원 짜리 동전 -> %d개" % c50)
print("10원 짜리 동전 -> %d개" % c10)
print("교환하지 못한 돈-> %d원" % money)
