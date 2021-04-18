import math
N = 10**6 + 1
prime = [True for i in range(N+1)]
prime[0],prime[1] = False,False
 
p = 2
while p*p<N:
    if prime[p]:
        for p1 in range(p*p,N,p):
            prime[p1]=False
    p+=1
 
n = int(input())
l = list(map(int,input().split()))
 
for x in l:
    X = math.sqrt(x)
    if int(X)==X and prime[int(X)] == True:
        print("YES")
    else:
        print("NO")
