nums = [2,0,2,1,1,0]

low = 0 
mid =0
high = len(nums) - 1

while(mid <= high):
    if(nums[mid] == 0): 
        temp = nums[mid]
        nums[mid] = nums[low]
        nums[low] = temp
        mid+=1
        low+=1
    elif(nums[mid] == 2):
        temp = nums[high]
        nums[high]  = nums[mid]
        nums[mid] = temp
        high -=1
    else:
        mid+=1


print(nums)