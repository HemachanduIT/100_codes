# input:{{{}}}
#     chandu
# output:
#     {{{chandu}}}

        
def concatestring(s1,s2):
    res=list(s1)
    mid=len(res)//2
    res.insert(mid,s2)
    return ''.join(res)
s1=input()
s2=input()
print(concatestring(s1,s2))
