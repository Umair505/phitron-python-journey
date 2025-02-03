from Users import User
from bank_object import bank
def user_interface():
    option=input("log in or register ? l/r : ").lower()
    if option=='r':
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        address=input("Enter your address: ")
        account_type=input("Enter your account type: ")
        password=input("Enter your password : ")
        us=User(name=name,email=email,address=address,account_type=account_type,password=password)
        while True:
            print("1.Diposite Money")
            print("2.Withdraw Money")
            print("3.Show balance")
            print("4.check transection history")
            print("5.Transfer Money")
            print("6.Main manu")
            choice=int(input("Enter the option: "))
            if choice==1:
                money=int(input("Enter the diposite amount: "))
                us.diposit(bank,money)

            elif choice==2:
                amount=int(input("Enter the amount for Withdraw: "))
                us.wihdraw(bank,amount)
            elif choice==3:
                us.show_balance()
            elif choice==4:
                us.check_history()
            elif choice==5:
                id=int(input("Enter the account id: "))
                amount=int(input("Enter the amount: "))
                us.transfer_money(bank,id,amount)
            elif choice==6:
                break
            else:
                print("Please chooice correct option !!!")
    elif option=='l':
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        us=bank.valid_user_or_not(email,password)
        if us:
            while True:
                print("1.Diposite Money")
                print("2.Withdraw Money")
                print("3.Show balance")
                print("4.check transection history")
                print("5.Transfer Money")
                print("6.Main manu")
                choice=int(input("Enter the option: "))
                if choice==1:
                    money=int(input("Enter the diposite amount: "))
                    us.diposit(bank,money)

                elif choice==2:
                    amount=int(input("Enter the amount for Withdraw: "))
                    us.wihdraw(bank,amount)
                elif choice==3:
                    us.show_balance()
                elif choice==4:
                    us.transection_history()
                elif choice==5:
                    id=int(input("Enter the account id: "))
                    amount=int(input("Enter the amount: "))
                    us.transfer_money(bank,id,amount)
                elif choice==6:
                    break
                else:
                    print("Please chooice correct option !!!")
        else:
            print("Sorry you give wrong information")
    else:
        print("Sorry you need to chooice l or r !")