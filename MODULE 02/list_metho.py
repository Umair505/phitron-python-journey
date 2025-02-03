numbers = [12,45,98,68]
numbers.append(56)
print(numbers)

numbers.insert(2,71)
numbers.insert(0,10)
print(numbers)
if 98 in numbers:
  numbers.remove(98)
print(numbers)

last = numbers.pop()
print(last)
if 71 in numbers:
    index = numbers.index(71)
index2 = numbers.index(45)
print(index,index2)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")

numbers =[7,6,5,3,3,2,1]
print(numbers[-4])

numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])
