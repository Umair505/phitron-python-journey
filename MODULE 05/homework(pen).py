#Pen class.Create three object with differen instance attribute
class pen:
    menufactured = 'China'
    #constructor
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_pen = pen('Moinul','Metador Alltime',6)
print(my_pen.owner,my_pen.brand,my_pen.price)