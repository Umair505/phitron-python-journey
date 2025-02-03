numbers = [12,56,98,78,56,12,26,98]
person1 = ['Moinul Islam','Chittagong',23,'Student']
#key value pair
#Dictionary
#object
#hash table
#overlap with set
person = {'Name':'Moinul Islam','Address':'Chattogram','Age':23,'Job':'Student'}
print(person)
print(person['Job'])
print(person.keys())
print(person.values())

person['Language'] = 'Python'
person['Name'] = 'Umair'
print(person)

del person['Age']
print(person)

#special dictionary looping
for key,value in person.items():
    print(key,value)

