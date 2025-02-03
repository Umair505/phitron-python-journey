from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
frq = defaultdict(int)
for num in arr:
    frq[num]+=1
sum = 0
for key,value in frq.items():
    if(value>=key):
        sum +=value - key
    else:
        sum+=value
print(sum)  