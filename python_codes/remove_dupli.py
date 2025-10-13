arr=[2,1,4,5,3,6,7,8,2,3,1]
# <----------------------------------->
print(list(set(arr)))
# <--------------------------------------->
# res=[]
# for i in arr:
#     if i not in res:
#         res.append(i)
# print(res)
# <-------------------------------------------->
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for k,v in d.items():
#     if v==1:
#         print(k,end='')

# output:
#     [1, 2, 3, 4, 5, 6, 7, 8]