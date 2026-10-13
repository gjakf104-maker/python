
#일한 시간(시간 단위) 입력: 18
#총 급여: 180000원
#--------------------
#10,000원권 : 18장
#1,000원권  : 0장
#남은 잔돈  : 0원






time = int(input("일한 시간 입력 :"))
recharge = [10_000, 1_000]

money = 10_000 * time
rnt = 0

print(f"총 급여 :{money}원")


for r in recharge :
    rnt = money // r
    print("%d원 짜리 지폐 -> %d장" %(r,rnt))
    money %= r


print("남은 잔돈 : %d원" %money)
    
