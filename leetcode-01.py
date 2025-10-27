nums = [3,2,4]
target = 6
j = 1
n = len(nums)
ans = []
i = 0
while(i<n and j < n ):
    if(nums[i]+nums[j]==target):
        ans.append(i)
        ans.append(j)
    j+=1
    if(j==n):
        i+=1
        j=i+1
print(ans)
print("End of Loop")