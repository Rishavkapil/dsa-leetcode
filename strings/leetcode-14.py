strs = ["flower", "flow","flight"]
# strs = [""]

# print(type(strs))
# print(strs[0][1])

# ptr = 0
# ltn = ""
# # print(strs[1])
# for i in range(0,len(strs)+1):
#     if(strs[i][ptr] == strs[i+1][ptr]):
#         ltn = ltn + strs[i][ptr]
#         ptr+=1
#     # print(i)
# print(ltn)

strs.sort()
# print(strs)
# print(strs[0])
# print(strs[-1])

first  = strs[0]
last = strs[-1]
ans = ""
for i in range(min(len(first),len(last))):
    if(first[i]!=last[i]):
        break
    ans+=last[i]

print(ans)
    