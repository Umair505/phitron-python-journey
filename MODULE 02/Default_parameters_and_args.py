# def sum(num1,num2):
#     result = num1 + num2
#     return result
# total = sum(99,11)
# print(total)

#args

def all_sum(*numbers):
    print(numbers)
    sum  = 0
    for num in numbers:
        #print(num)
        sum = sum + num
    return sum
total2 = all_sum(45,46,47,49)
print("all sum: ",total2)
