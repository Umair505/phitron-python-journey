class shop:
    cart =[]#cart is a class attribute
    def __init__(self,buyer):
        self.buyer = buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)

mehzabeen = shop('meh jabin')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = shop('nishoo')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)