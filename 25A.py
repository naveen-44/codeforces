n = int(input())
l = list(map(int,input().split()))
epos = -1
e = 0
opos = -1
for i in range(len(l)):
    if l[i]%2==0:
        e+=1
        epos = i+1
    else:
        opos = i+1
if e == 1:
    print(epos)
else:
    print(opos)
