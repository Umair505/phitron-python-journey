numbers = [45,87,65,43,85,60,14,26,61,70]
odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)
#shortcut
odd_nums = [num for num in numbers if num%2 == 1 and num % 5 == 0]#meaningful na
print(odd_nums)

players = ['Sakib','Musfik','Tamim','Mustafiz']
ages = [38,38,32]

age_comb = []
for player in players:
    print('Player:',player)
    for age in ages:
        # print(player,age)
        age_comb.append([player,age])
print(age_comb)

age_comb2 = [(player,age) for player in players for age in ages]
print(age_comb2)