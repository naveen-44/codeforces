n = int(input())
l = list(map(int, input().split()))
l1 = sorted(l)
s = sum(l)
c_sum = 0
count = 0
for i in range(len(l1)-1, -1, -1):
    x = l1[i]
    if c_sum <= (s//2):
        c_sum += x
        count += 1
    else:
        break
print(count)
