num1 = int(input("교환할 돈을 입력 :"))


result1 = num1/500; recharge =num1%500 
print(f"500원짜리 동전 --> {result1}")

result2 = result1//100
print(f"100원짜리 동전 --> {result2}")

result3 = result2//50
print(f"50원짜리 동전 --> {result3}")

result4 = result3//10
print(f"10원짜리 동전 --> {result4}")

result5 = result3%10
print(f"교환하지 못한 잔돈 --> {result5}")
