# Find the Largest element in the array 

nums = [43,2,4,1,53,10]


# printing the array 

print(nums)

largest = -1

for i in range(0,len(nums)):
    if(nums[i] > largest):
        largest = nums[i]

# printing the largest element 

print("The largest element in the array is : " , largest)


# we can also solve this by sorting the array and return the last element but it isn't a good apporach
