arr=[1,2,3,4,6]
# for i in range(1,len(arr)+1):
#     if i not in arr:
#         print(i)
# <--------------------------------------->
lenn=arr[-1]
summ1=lenn*(lenn+1)//2
summ2=sum(arr)
print(abs(summ1-summ2))

# output:
#     5
        