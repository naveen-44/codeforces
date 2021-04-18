s = input().lower()
ans = ''
vow = ['a','e','i','o','u','y']
for i in s:
    if i not in vow:
        ans = ans + '.' + i
print(ans)
