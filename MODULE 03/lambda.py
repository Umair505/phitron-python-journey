#lambda 1 line a function likhe fela jai
# def double(x):
#     return x*2

double = lambda num : num*2
squared = lambda num : num*num
ouput = squared(9)
result = double(44)
# print(result,ouput)

add = lambda x,y: x + y
sum = add(11,33)
# print(sum)

numbers = [12,5,98,78,56,12,6,98]
# doubled_nums = map(double,numbers)
doubled_nums = map(lambda x:x*2,numbers)
squared_nums = map(lambda x:x*x,numbers)
print(list(squared_nums))
print(numbers)
print(list(doubled_nums))

actors = [
    {'Name':'Sabana','age':65},
    {'Name':'Shabnur','age':45},
    {'Name':'Sabila noor','age':25},
    {'Name':'Srabonti','age':32},
    {'Name':'Shawon','age':38},
]
juniors = filter(lambda actor : actor['age']<40,actors)
print(list(juniors))
Fivers = filter(lambda actor : actor['age']%5==0,actors)
print(list(Fivers))


numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])

numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

num = lambda a:a*a
print(num(2**2))