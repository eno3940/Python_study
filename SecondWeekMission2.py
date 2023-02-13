class Car():

    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels
    
class Bike(Car): #부모 클래스 Car 상속
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels) # 부모 객체 사용
        self.size = size # 속성값 추가

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)