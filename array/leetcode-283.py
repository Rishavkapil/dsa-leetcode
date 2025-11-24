# nums = [0,1,0,3,12]
# nums = [1,0,1]
nums = [4,2,4,0,0,3,0,0,5,1,0]

n = len(nums)
ctr = 0
for ptr in range(1,n):
    if(nums[ptr]!= 0 and nums[ctr] == 0 ):
        temp = nums[ctr]
        nums[ctr]=nums[ptr]
        nums[ptr]=temp
        ctr+=1
    elif(nums[ctr]!=0):
        ctr+=1
print(nums)