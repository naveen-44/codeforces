s = input()
ss = 'hello'
flag = False
k = 0
for i in range(len(s)):
    if(k<len(ss) and s[i]==ss[k]):
        k+=1
if(k==len(ss)):
    print("YES")
else:
    print("NO")
