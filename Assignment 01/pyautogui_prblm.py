import pyautogui
n = int(input())


for i in range(1, n + 1):
    pyautogui.write('# '*i, interval = 0.10)
    pyautogui.press('enter')


import pyautogui
N =int(input())

for i in range(1,N+1):
    pyautogui.write("#"*i)
    pyautogui.press('Enter')


import pyautogui

N = int(input("Enter the number of levels: "))

for i in range(1, N + 1):
    pyautogui.write("#" * i)
    pyautogui.press('enter')  # Use 'enter' instead of 'Enter'


list1 = [1,2,3,4,5,6]
print(list1)
list1[0] = 10
list1.append(20)
list1.remove(5)
print(list1)

Dict = {'name':'Moinul','age':22,'city':'Chittagong'}
print(dict['name'])
Dict['age'] = 23
print(Dict)
Dict['job'] = 'Student'
del Dict['age']
print(Dict)
