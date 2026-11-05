'''
class Car:
    # 멤버 필드 선언
    color = ""
    speed = 0
    # 멤버 메서드 선언
    def upSpeed(self,value):
        self.speed += value

    def dowmSpeed(self,value):
        self.speed -= value

#핸드폰 개통         
myCar1 = Car() # 인스턴스(객체)
myCar1.color = 'RED'
myCar1.speed = 0 # 인스턴스 변수 

myCar2 = Car() # 인스턴스(객체)
myCar2.color = 'Black'
myCar2.speed = 0



myCar1.upSpeed(30)
print(myCar1)
'''


class Calculator:
def __init__(self):
      self.result =0

def add(self, num):
    self.result += num
    return self.result

cal1 = Calculator()
cal2 = Calculator()
