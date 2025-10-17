def common_ele(a1,a2):
    res=[]
    for i in a1:
        if i in a2:
            res.append(i)
    return res
    # for i in a2:
    #     if i in a1:
    #         res.append(i)
    # return set(res)
    
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
print(common_ele(a1,a2))