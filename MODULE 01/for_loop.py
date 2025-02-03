# numbers = [5,10,14,50,20,25]
# sum = 0
# for num in numbers:
#     print(num)
#     sum+=num
#     if sum>20:
#         print('Bigger sum',sum)
# print(sum)

# text = 'Pagla Howar'
# for char in text:
#     print(char)

#nums = [1,2,3,4,5,6,7,8,9,10]

#print(range(1,10))#1-9 print korbe
for i in range(1,10):
    print(i)

for i in range(1,10,2):#2 kore barbe protthekbar
    print(i)

for i, value in enumerate(range(1,10)):
    print('Index:',i,'Value:',value)