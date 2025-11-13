nums = [6,10,6]

# printing the array
print(nums)
n = len(nums)

# printing the size of array 
print("Size of Array : " , n)


# Trying two pointer approach 

left = 0
right = 1

# taking false counter 

falseCounter = 0
while(left <=right and right < n):
    if(nums[left]<= nums[right]):
        left+=1
        right+=1
    else:
        falseCounter+=1
        left+=1
        right+=1

# taking right to the start of the array

right = 0
print("left = " , nums[left] , "right = ", nums[right])

if(nums[left] <= nums[right]):
    pass
else:
    falseCounter+=1
    # print("False")

if(falseCounter==0 or falseCounter<2):
    print("True")
else:
    print("False")