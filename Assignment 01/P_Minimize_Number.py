n = int(input())
num = input().split()
a = []
for val in num:
    a.append(int(val))  

cnt = 0
while True:
    flag = False
    for i in range(len(a)): 
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            flag = True
            break
    if flag:
        break  
    cnt += 1

print(cnt)
