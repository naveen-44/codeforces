n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    x = a%b
    if x == 0:
        print(x)
    elif(a-x)%b==0:
        print(b-x)
    else:
        print(x)
