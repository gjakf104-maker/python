#(1) 객체를 통해서 변경하는 방법
'''class Car:
    # 자동차를 표현하는 속성(변수)
    # 자동차를 이용하기 위한 함수(제조회사, 모델, 생산년도)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 0 # 추가된 멤버 변수 

    #출력 함수를 직접 정의한다
    #속성 값들을 하나로 합치기 위해서 선언    
    def get_name(self):
        c_name = f"{self.year} {self.make} {self.model}"
        return c_name.title()

    # 주행거리 km
    def c_km(self):
        print(f"이 자동차의 주행거리는 {self.km}km이다")
    
my_car1 = Car('kia','k5',2026)

my_car2 = Car('hyundai','genesis',2026)
print(my_car1.get_name())
my_car1.km = 20
my_car1.c_km()
print(my_car2.get_name())

#2 메서드를 통해서 값을 변경
class Car:
    # 자동차를 표현하는 속성(변수)
    # 자동차를 이용하기 위한 함수(제조회사, 모델, 생산년도)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 0 # 추가된 멤버 변수 

    #출력 함수를 직접 정의한다
    #속성 값들을 하나로 합치기 위해서 선언    
    def get_name(self):
        c_name = f"{self.year} {self.make} {self.model}"
        return c_name.title()

    # 주행거리 km
    def c_km(self):
        print(f"이 자동차의 주행거리는 {self.km}km이다")

    #메서드를 통해서 속성값 변경하는 함수
    def update_km(self,km):
        self.km = km

        
my_car1 = Car('kia','k5',2026)

print(my_car1.get_name())
my_car1.update_km(25)
my_car1.c_km()
'''

#3 메서드를 통해 일정한 값을 더함
class Car:
    # 자동차를 표현하는 속성(변수)
    # 자동차를 이용하기 위한 함수(제조회사, 모델, 생산년도)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 0 # 추가된 멤버 변수 

    #출력 함수를 직접 정의한다
    #속성 값들을 하나로 합치기 위해서 선언    
    def get_name(self):
        c_name = f"{self.year} {self.make} {self.model}"
        return c_name.title()

    # 주행거리 km
    def c_km(self):
        print(f"이 자동차의 주행거리는 {self.km}km이다")

    #메서드를 통해서 속성값 변경하는 함수
    def update_km(self,km):
        if km >= self.km:
            self.km = km
        else:
            print("현재 km값을 되돌릴 수 없다")

    #일정한 값을 주어 그 값만큼 늘린다
    def increment_km(self,km):
        self.km += km

# 전기 자동차 클래스를 선언하고  기존 클래스 상속(super()-->부모 클래스를 상속)
class Electric(Car):
    def __init__(self,make, model,year):
        super().__init__(make, model, year) #self 생략이 가능
        self.battery_size = 100

        
    def b_battery(self):
        print(f"이 전기자동차의 배터리 사이즈는 {self.battery_size}kw입니다")
    
my_car1 = Car('kia','k5',2026)
my_car2 = Electric('hyundai','ionic5',2025)
print(my_car2.get_name())
print(my_car1.get_name())
my_car2.b_battery()
