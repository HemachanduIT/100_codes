#factorial
# n=int(input())
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)


#palindrome n0
# n=int(input())
# r=0
# k=n
# while n!=0:
#     r=r*10+n%10
#     n//=10
# if k==r:
#     print("palindrome")
# else:
#     print("not")

#palindrome string
# s=input()
# r=''
# for i in s:
#     r=i+r
# if r==s:
#     print('yes')
# else:
#     print('not')
# # if s==s[::-1]:
#     print('palindrome')
# else:
#     print('not')

#swaping
# a,b=10,20
# print('before ',a,b)
# a,b=b,a
# print('after',a,b)

#prime no
# from math import sqrt
# n=int(input())
# c=True
# for i in range(2,int(sqrt(n))+1):
#     if n%i==0:
#         c=False
#         break
# if c:
#     print('prime')
# else:
#     print('not')

#prime series
# import math
# for i in range(1,51):
#     c=True
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:
#             c=False
#     if c:
#         print(i,end=' ')

#vowels present or not
# s=input()
# v='aeiouAEIOU'
# for i in s:
#     if i in v:
#         print('vowels presnet')
#         break
# else:
#         print('not present')

#count vowels in string
# s=input()
# c=0
# v='aeiouAEIOU'
# for i in s:
#     if i in v:
#         c+=1
# print('count of vowekls is',c)

#odd or even
# n=int(input())
# if n%2==0:
#     print('even')
# else:
#     print('odd')

# s='02468'
# k=str(n)
# if k[-1] in s:
#     print(n,'is even')
# else:
#     print('odd')

# if n&1==0:
#     print('even')
# else:
#     print('0dd')

#biggest string in sentence

    