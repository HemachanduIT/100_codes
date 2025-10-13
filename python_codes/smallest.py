arr=[3,4,2,1,5,6,76,4,-5]
# print(min(arr))
minn=arr[0]
for i in range(len(arr)):
    if arr[i]<=minn:
        minn=arr[i]
print(minn)

# output:
#     -5