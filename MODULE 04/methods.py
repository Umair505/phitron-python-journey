def call():
    print('Calling someone i dont know')
    return 'call done'

class phone:
    price = 12000
    color = 'Blue'
    brand = 'samsung'
    features = ['Camera','Speaker','Hammer']
    def call(self):
        print('calling one person')
    def send_sms(self,Phone,sms):
        text = f'sending SMS to:{Phone} and message:{sms}'
        return text
my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(12451,'I forgot to miss you')
print(result)