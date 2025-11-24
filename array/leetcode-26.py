# my approach : I'll be using two pointer approach in this, 
# i'll take two pointers 1. ctr 2. ptr,
# ctr will be pointing to current latest unique element and ptr will be traversing the whole list. 
# If both nums[ctr] and nums[ptr] matches, then we'll move ptr by 1 
# if both are different i.e nums[ctr]!=nums[ptr], then we'll replace nums[ctr+1] with nums[ptr] and increment both. 


nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]

# lets take the size of list as n 

n = len(nums)

ctr = 0
count = 1

for ptr in range(1,n):
    if (nums[ctr]==nums[ptr]):
        continue
    else:
        count+=1
        nums[ctr+1]=nums[ptr]
        ctr+=1

print("Total unique elements = ", count)
print("List after swaping unique elements in place: " , nums)