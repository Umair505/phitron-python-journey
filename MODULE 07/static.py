# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = [] #class attribute #static attribute
    origin = 'china'
    
    def __init__(self, name, location) -> None:
        self.name = name  # instance attribute
        self.location = location
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinmu na just ac er hawa khaite aschi', item)


basundara = Shopping('basu en dhara', 'not popular location')
basundara.purchase('lungi', 500, 1000)
# Shopping.purchase(2,3,3)
basundara.hudai_dekhi('Lungi')
Shopping.hudai_dekhi('lungi')
Shopping.multiply(2,3)#static method
basundara.multiply(2,3)#using instance