n = int(input())
l = list(map(int,input().split()))
l1 = sorted(l)
s = sum(l)
csum = 0
count = 0
for i in range(len(l1)-1,-1,-1):
    x = l1[i]
    if csum<=(s//2) :
        csum+=x
        count+=1
    else:
        break
print(count)