# input:
#     10
# output:
#     0 1 1 2 3 5 8 13 21 34

def fib(k):
    if k==1:
        return 0
    elif k==2:
        return 1
    else:
        return fib(k-2)+fib(k-1)
n=int(input())
for i in range(1,n+1):
    print(fib(i),end=' ')
# n=int(input())
# a=0
# b=1
# s=0
# print(a,b,end=' ')
# for i in range(2,n):
#     s=a+b
#     print(s,end=' ')
#     a=b
#     b=s
