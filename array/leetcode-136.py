# nums = [2,2,1]
nums = [4,1,2,1,2]

ans = nums[0]

for i in range(1,len(nums)):
    ans ^= nums[i]
print("The only unique element is : " , ans)