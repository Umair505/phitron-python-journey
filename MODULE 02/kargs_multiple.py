def full_name(first,last):
    name = f'{first} {last}'
    return name
# take parameters in order(serial wise)
# name = full_name('Moinul','Islam')
name = full_name(last = 'Islam', first ='Moinul')
print(name)

def famous_name(first,last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key, value in additional.items():
        print(key,value)
    return name

name = famous_name(first='Moinul', last = 'Islam',title = 'Student',title2= "Programmer",last2 ='Umair')
print(name)

#def function_name(num1,num2,*args,**kargs):

def a_lot(num1,num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    # return [sum,mult,remain] list akare
    return sum,mult,remain
everything = a_lot(55,21)
print(everything)