s = input()
l =0
r = 0
idx = 0
ans =""
arr =[]
for i in s:
    ans += i
    if i == 'L':
        l=l+1
    else :
        r = r+1
    if l==r:
        arr.append(ans)
        ans =""
        idx=idx+1
        l = 0
        r = 0
print(idx)
for char in arr:
    print(char)