# input:
#     5
# output:
#     120
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
# n=int(input())
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)