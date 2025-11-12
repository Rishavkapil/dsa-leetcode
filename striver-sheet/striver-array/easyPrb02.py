# Find the second largest element in the array 

nums = [434,23,43,24,434]

# printing the array 

print(nums)

# approach : first we'll find the largest and then replace it with -1 and then again find the largest from the new array 

largest = -1
IndexOfLargest = -1
for i in range(0,len(nums)):
    if(nums[i]>largest):
        largest = nums[i]
        IndexOfLargest = i
nums[IndexOfLargest] = -1
## printing the new array after replacing the largest with -1
print(nums)

## reseting the largest 
largest = -1

for i in range(0,len(nums)):
    if(nums[i]>largest):
        largest = nums[i]


## Printing the second largest

print(largest)