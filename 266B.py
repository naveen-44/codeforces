def fun(q):
    ans = []
    for i in q:
        ans.append(i)
    for i in range(1,len(q)):
        if q[i]=="G" and q[i-1] == "B":
            ans[i-1] = "G"
            ans[i] = "B"
            
    return ans

n,t = raw_input().split()
q = raw_input()
n = int(n)
t = int(t)
Q = []
for qq in q:
    Q.append(qq)
ans = Q
for i in range(t):
    ans = fun(ans)
res = ''
for i in ans:
    res+=i
print(res)
