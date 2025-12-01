# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]

count = 0 
maxCount = 0
for i in range(0,len(nums)):
    if(nums[i] == 0):
        count = 0
    else: 
        count+=1
        maxCount = max(count,maxCount)
print("The maximum number of consecutive 1's are : " , maxCount)