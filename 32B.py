s = input()
k = 0
ans = ''
while k < len(s):
    if s[k] == '.':
        ans += '0'
        k += 1
    else:
        if s[k+1] == '.':
            ans += '1'
        else:
            ans += '2'
        k += 2
print(ans)
