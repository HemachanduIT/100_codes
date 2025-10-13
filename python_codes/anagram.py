# input:
#     listen
#     silent
# output:
#     anagram
s1=input()
s2=input()
# <------------------------------>
# if sorted(s1)==sorted(s2):
#     print("anagram")
# else:
#     print("not a anagram")
# <---------------------------------->
# from collections import Counter
# if Counter(s1)==Counter(s2):
#     print("Anagram")
# else:
#     print("not a anagram")
# <----------------------------------->
flag=True
if len(s1)==len(s2):
    for i in s1:
        if i not in s2:
            flag=False
    for i in s2:
        if i not in s1:
            flag=False
else:
    flag=False
if flag:
    print("anagram")
else:
    print("not a anagram")