nums1 = [1,3]
nums2 = [2,4]
newArr = []
n = len(nums1)
m = len(nums2)
print("Size of nums1 = " , n , "Size of nums2 = ", m)

i = 0
j = 0

while(i < n and j<m):
    if(nums1[i] >= nums2[j]):
        newArr.append(nums2[j])
        j+=1
    else:
        newArr.append(nums1[i])
        i+=1

while(i<n):
    newArr.append(nums1[i])
    i+=1
while(j<m):
    newArr.append(nums2[j])
    j+=1
print(newArr)

median = -1
s = len(newArr)
print("Length of new array = ", s)
if (s%2==0):
    median= (newArr[s//2] + newArr[(s-1)//2])/2
else:
    median = newArr[s//2]
print("Median = ", median)
