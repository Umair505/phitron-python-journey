class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    
    def remove_item(self,item_name):
        for item in self.cart:
            if item['item']==item_name:
                self.cart.remove(item)
    
    # def remove_item(self, item_name):
    #     for item in self.cart:

    #         if item['item'] == item_name:
    #           self.cart.remove(item)
    #           print(f"{item_name} removed from the cart.")
    #           return
    #     print(f"{item_name} not found in the cart.")


    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total +=item['price'] * item['quantity']
        print('Total price',total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra =amount - total
            print(f'Here is your extra money: {extra}')
moinul = shopping('Moinul Islam')
moinul.add_to_cart('alu',50,6)
moinul.add_to_cart('Dim',12,24)
moinul.add_to_cart('Rice',50,5)
moinul.remove_item('alu')
moinul.remove_item('Dim')
print(moinul.cart)

# moinul.checkout(600)
moinul.checkout(1600)