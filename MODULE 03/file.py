# .csv comma separted value
#.txt text file

# with open('message.txt','w') as file:
#     file.write('I love you, pyton!')

# with open('message.txt','a') as file:
#     file.write('I love you, pyton!')

with open('message.txt','r') as file:
    text = file.read()
    print(text)

# with open('message.txt','a') as file:
#     file.write('I love you, pyton!')