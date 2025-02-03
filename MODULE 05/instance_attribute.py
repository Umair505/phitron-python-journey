class shop:
    shopping_mall = 'Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] #cart is a instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)
    
mehjabin = shop('Meh jab een')
mehjabin.add_to_cart('shoe')
mehjabin.add_to_cart('phone')
print(mehjabin.cart)

nisho = shop('Nishoo bhai')
nisho.add_to_cart('Pent')
nisho.add_to_cart('Watch')
print(nisho.cart)

apurb = shop('Age purbo chilo')
apurb.add_to_cart('Chiruni')
print(apurb.cart)