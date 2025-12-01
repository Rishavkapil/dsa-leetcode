# nums = [2,2,1]

ans = nums[0]

for i in range(1,len(nums)):
    ans ^= nums[i]
print("The only unique element is : " , ans)