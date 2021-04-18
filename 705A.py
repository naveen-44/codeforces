def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
nums =[]
for i in range(4):
    n = int(input())
    nums.append(n)
nums = sorted(nums)
print(nums)
N = int(input())
ans = []
for i in range(N+1):
    for j in range(4):
        print(nums[j])
