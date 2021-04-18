nums =[]
for i in range(4):
    n = int(input())
    nums.append(n)
nums = sorted(nums)
N = int(input())
if nums[0] == 1:
    print(N)
else:
    ans = 0
    for i in range(1,N+1):
        if i%nums[0]==0 or i%nums[1]==0 or i%nums[2]==0 or i%nums[3]==0:
            ans+=1
    print(ans)
