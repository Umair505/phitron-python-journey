from Users import Admin
from bank_object import bank
def admin_interface():
    option=input("log in or registation ? l/r: ").lower()
    if option=='r' and  len(bank.admin)==1:
          option='l'
          print("Admin already exit you need to log in\n")
    if option=='r':
                
          name=input("Enter your name: ")
          email=input("Enter your email: ")
          address=input("Enter your address: ")
          account_type=input("Enter the type of account: ")
          password=input("Enter your password: ")
          ad=Admin(name=name,email=email,address=address,account_type=account_type,password=password)
          while True:      
                  print("1.delete any user account ")
                  print("2.show all user accounts list")
                  print("3.check the total available balance of the bank ")
                  print("4.check the total loan amount")
                  print("5.on or off the loan feature of the bank")
                  print("6.Main manu")
                  print("7.Add money to the bank: ")
                  choice=int(input("Choice the option: "))
                  if choice==1:
                        id=int(input("Enter the user id: "))
                        ad.delete_user(bank,id)
                  elif choice==2:
                        ad.see_all_user_account_list(bank)
                  elif choice==3:
                        ad.show_bank_balance(bank)
                  elif choice==4:
                        ad.show_total_loans_amount(bank)
                  elif choice==5:
                        Set=bool(input("Enter Ture or Flase to on or off loan Feature: "))
                        ad.set_loan_status(bank,Set)
                  elif choice==6:
                        break
                  elif choice==7:
                        money=int(input("Enter the amount: "))
                        bank.add_money(money)
                  else:
                        print("Please chooce the correct option: ")
      
                        
    elif option=='l':
          email=input("Enter your email: ")
          password=input("Enter your password: ")
          ad=bank.valid_admin_or_not(email,password)
          if ad:       
            while True:   
                        print("1.delete any user account ")
                        print("2.show all user accounts list")
                        print("3.check the total available balance of the bank ")
                        print("4.check the total loan amount")
                        print("5.on or off the loan feature of the bank")
                        print("6.Main manu")
                        print("7.Add money to the bank")
                        choice=int(input("Choice the option: "))
                        if choice==1:
                              id=int(input("Enter the user id: "))
                              ad.delete_user(bank,id)
                        elif choice==2:
                              ad.see_all_user_account_list(bank)
                        elif choice==3:
                              ad.show_bank_balance(bank)
                        elif choice==4:
                              ad.show_total_loans_amount(bank)
                        elif choice==5:
                              Set=bool(input("Enter Ture or Flase to on or off loan Feature: "))
                              ad.set_loan_status(bank,Set)
                        elif choice==6:
                              break
                        elif choice==7:
                              money=int(input("Enter the amount: "))
                              bank.add_money(money)
                        else:
                              print("Please chooce the correct option: ")    
          else:
                print("The admin not exist !") 
    else:
          print("Sorry you need to chooice l or r !")

          
    
     

       
        
        