'''
# 수학에 관련된 기능을 사용하려면
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        self.radius =radius
    def circleArea(self):
        return math.pi *(self.radius**2)

circle =Circle(10)
print("원의 넓이 :", circle.circleArea())
print()
print("반지름에 접근하여 반지름값 출력")
print(circle.radius)

# 수학에 관련된 기능을 사용하려면
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        self.r =radius
    def circleArea(self):
        return math.pi *(self.r**2)

c1 =Circle(6)
print("원의 넓이 :", c1.circleArea())
print()
print("반지름에 접근하여 반지름값 출력")
print(c1.r)
'''
'''import math 
class Circle:
    def __init__(self,radius):
        self.r = radius
    def Cir(self):
        return 4/3 * math.pi *(self.r**3)

cle = Circle(5)
print("구의 부피:" ,cle.Cir())
#######################################
import math 
class Circle:
    def __init__(self,radius):
        self.__r =radius
    def circleArea(self):
        return math.pi *(self.__r**2)
# getter/setter 함수 선언
    def getRadius(self):
        return self.__r

    def setRadius(self,value):
        self.__r = value

c1 =Circle(6)
print(f"원의 넓이 : {c1.circleArea():.2f}")
print()
print("반지름에 접근하여 반지름값 출력")
print(c1.getRadius())
'''


