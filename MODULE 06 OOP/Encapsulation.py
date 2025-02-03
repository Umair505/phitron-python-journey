#Encapsulation ---> Hide details
#Access modifier: public,protected,private
class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name #public attribute
        self._branch = 'Banani'#protected
        self.__balance = initial_deposit#private class chara onno kothao accessivle na

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nai'
    def get_balance(self):
        return self.__balance

rafsan = Bank('Choto Bhai',10000)
rafsan.holder_name = 'Boro Bhai'
print(rafsan.holder_name)
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan._branch)

#jor kore access
print(dir(rafsan))
print(rafsan._Bank__balance)