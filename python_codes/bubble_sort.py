def bubble_sort(arr):
    pass
    flag=True
    while flag:
        flag=False
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=True
    return arr
            

arr=list(map(int,input().split()))
print(bubble_sort(arr))