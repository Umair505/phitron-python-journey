def famous_name(first,last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key, value in additional.items():
        print(key,value)
    return name

name = famous_name(first='Moinul', last = 'Islam',title = 'Student',title2= "Programmer",last2 ='Umair')
print(name)