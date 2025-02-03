class Phone:
    manufactured = 'China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):
        text = f'Sending to: {phone} {sms}'
        print(text)

my_phone = Phone('Moinul','Xiaomi','15000')
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone = Phone('Nusrat','Iphone',150000)
print(her_phone.owner,her_phone.price,her_phone.brand)

dad_phone = Phone('abbu','Nokia',3000)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)
