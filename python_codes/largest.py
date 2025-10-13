# arr=list(map(int,input().split()))
# <------------------------------------------>
# print(max(arr))
# <------------------------------------------->
arr=[3,4,2,1,5,6,76,4,0]
maxx=arr[0]
for i in range(len(arr)):
    if arr[i]>=maxx:
        maxx=arr[i]
print(maxx)

# output:
#     76