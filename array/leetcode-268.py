def find_missing(nums):
    n = len(nums)
    nums.sort()
    print(nums)
    flag = 0
    for i in range(0,n):
        if(nums[i] != i):
            flag = 1
            return i
    if(flag == 0):
        return n

# nums = [0,1]
nums  = [1,0,2,4]

print(find_missing(nums))