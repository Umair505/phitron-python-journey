#poly ---> many(multiple)
#morph --> shape
#eki jinish onk gula rup thakte pare
class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Meow meaow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Bhaow Bhawoa")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Soooooo')


don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('Gora gori')

animals =[don,shepard,mess,less]
for animal in animals:
    animal.make_sound()