class Car:
    # 자동차를 표현하는 속성(변수)
    # 자동차를 이용하기 위한 함수

    # 제일 먼저 선언하는 것
    def __init__(self, make, model, year):
        # 속성을 초기화 
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0 # 추가된 멤버 변수 

    # 출력 함수를 직접 정의한다.
    # 속성 값들을 하나로 합치기 위해서 선언 
    def get_name(self):
        c_name = f"{self.year} {self.make} {self.model}"
        return c_name.title()

    # 주행거리
    def c_mileage(self):
        print(f"이 자동차의 주행거리는 {self.mileage}마일리지 입니다.")

    # 메서드를 통해서 속성값 변경 하는 함수
    def update_mileage(self, mileage):
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("현재 마일리지 값을 되돌릴수 없습니다.")

    #일정한 값을 주어서 그 값만큼 늘린다. 
    def increment_mileage(self, mileage):
        self.mileage += mileage

        
        

my_car1 = Car('kia', 'k9', 2026)
print(my_car1.get_name())

my_car1.update_mileage(25)
my_car1.c_mileage()

my_car1.increment_mileage(100)
my_car1.c_mileage()

















    
        
