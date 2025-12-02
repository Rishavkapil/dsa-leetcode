nums = [2,2,1,1,1,2,2]

s = set()
dc = {}
# print(type(s))

for i in nums:
    dc[i] = dc.get(i,0)+1 # this will try to get value for key i.e i , if i is not present it will return 0. 

for i in dc:
    if(dc[i] > len(nums)//2):
        # print(dc[i])
        print(i)
        break
print(dc)


