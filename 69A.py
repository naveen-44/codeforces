n = int(input())
xf,yf,zf = 0,0,0
for i in range(n):
    x,y,z = list(map(int,input().split()))
    xf+=x
    yf+=y
    zf+=z
if(xf==0 and yf ==0 and zf ==0):
    print("YES")
else:
    print("NO")
