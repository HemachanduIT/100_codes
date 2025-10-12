# input:
#     121
# output:
#     121 is palindrome
n=int(input())
k=n
r=0
while n!=0:
    r=r*10+n%10
    n//=10
if r==k:
    print(k,'is palindrome')
else:
    print(k,'is not palindrome')