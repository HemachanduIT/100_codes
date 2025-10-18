from collections import Counter
def max_occurence(s):
    d=Counter(s)
    # d={}
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    maxx=max(d.values())
    for k,v in d.items():
        if v==maxx:
            return k
        
            
s=input()
print(max_occurence(s))