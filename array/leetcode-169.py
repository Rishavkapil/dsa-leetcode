# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]

# s = set()
# dc = {}
# # print(type(s))

# for i in nums:
#     dc[i] = dc.get(i,0)+1 # this will try to get value for key i.e i , if i is not present it will return 0. 

# for i in dc:
#     if(dc[i] > len(nums)//2):
#         # print(dc[i])
#         print(i)
#         break
# print(dc)




## Now we'll try to solve this in O(1) space complexity 



nums.sort()
print(nums)

## Handling edge case when array has only 1 element
if(len(nums)==1):
    print(nums[0])

count = 0
for i in range(0,len(nums)-1):
    if(nums[i] == nums[i+1]):
        count+=1
        # print(count)
        if(count > (len(nums)//2)-1):
            print(nums[i])
            break
    else:
        count = 0