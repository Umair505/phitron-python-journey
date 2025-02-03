#list,array,collection is same (simple terms)
#index     0  1  2  3  4  5   6 7  8  9
numbers = [45,12,56,89,87,32,89,59,56,93]
#index    -9 -8 -7 -6  -5 -4   -3  -2  -1
print(numbers[4],numbers[-3])
#list (start : end) #start from the start index and stops befor the end index
print(numbers[2:6])

#list(start:end:step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[7:2:-1])#7 theke 2 e jabo 1 kore kombe
print(numbers[4:])
print(numbers[:5])
print(numbers[:])#shortcut to copy a list
print(numbers[::-1])#reverse hoye jabe