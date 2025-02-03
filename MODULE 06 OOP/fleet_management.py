#Ena poribohon
class Company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.manager = []
        self.supervisors = []

class Driver:
    def __init__(self,name,license,age) -> None:
        self.license = license
        self.name = name
        self.age = age

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self,start,destination):
        pass

class Passenger:
    pass

class Supervisors:
    pass

red_mia = Driver('a','123',32)


