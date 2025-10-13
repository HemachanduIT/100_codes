import sys
arr=[6,1,2,5,7,8]
# arr.sort()
# print("the 2nd largest elemtn is",arr[-2])
f,s=-2**63,-2**63
for i in arr:
    if i>f:
        s=f
        f=i
    elif i>s and i!=f:
        s=i
print(s)