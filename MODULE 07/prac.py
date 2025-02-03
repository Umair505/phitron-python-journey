class User:
    def __init__(self,name,age,weight,height) -> None:
        self._name = name
        self.__age = age
        self.weight = weight
        self.height = height
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value
    def weight(self):
        return self.weight
    
moinul = User('Moinul',23,65,4.4)
print(moinul.age)
moinul.age = 24
print(moinul.age)
    