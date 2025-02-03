from User_interface import user_interface
from Admin_inter_face import admin_interface
print("1.singn in or singup as Admin:")
print("2.sign in or sing up as User? : ")
print("3.Exit")
while True:
    choice=int(input("Choose any option between 1/2: "))
    if choice==1:
      admin_interface()
    elif choice==2:
      user_interface()
    elif choice==3:
      break
    else:
      print("please choose correct option ")