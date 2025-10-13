# input:
#     2 34 1 5 7 3 8 9
# output:
#     asc-->1 2 3 5 7 8 9 34
#     desc-->34 9 8 7 5 3 2 1
n=list(map(int,input().split()))
n.sort() #asc
n.sort(reverse=True)  #desc
print(*n)