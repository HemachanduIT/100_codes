def nonrepeat(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res=[k for k,v in d.items() if v==1]
    return res[0]
s=input()
print(nonrepeat(s))