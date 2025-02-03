name = 'Sakib Khan'
name2 = "Sakib khan"
name3 = """ 
    Sakib Khan
    number one
 """
nam = 'Sakib\'s Khan'#escape
print(nam)
#String is a sequence of character
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])#reverse
#mutable means changeable
#immutable means you can not change it
# name2[0] = 'R'
# print(name2)
if 'khan' in name2:
    print('Exists')
print(name2.upper())
print(name2.count())