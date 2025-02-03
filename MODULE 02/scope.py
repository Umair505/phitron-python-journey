balance = 3000

def buy_things(item,price):
    #local scope variable
    #you can acces global variable without using the global keyword
    #If you want to modify a global variable,you have to use the global keyword
    global balance
    print(balance)
    balance = balance - price
    print(f'balance after buying {item}',balance)
buy_things('Sunglass',1000)