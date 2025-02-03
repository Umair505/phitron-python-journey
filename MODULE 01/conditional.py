#in,not,not in ,is,is not
a = 1
boss = False
if a > 5 :
    print('5 er besi')
    print('koto beshi k jane')
elif a>3:
    print('Olpo boro')
elif a==2:
    print('2 er shoman')
else:
    print('5 er kom')

if boss is not True:
    print('Lunch er por asen')
else :
    print('Tel er baksho nia ashtechi boss k tell dibo')

#nested condition
    coin = 'head'
if boss == True:
    print('Boss you are joss')
    if coin == 'tail':
        print('batting')
    else :
        print('bowling')
else : 
    print('You are loss not a boss')

