def separation(n,s):
    # res=[]
    posi=[i for i in s if i>=0]
    neg=[i for i in s if i<0]
    res=posi+neg
    # print(*res)
    # return ''.join(res)
    return ' '.join(map(str,res))

n=int(input())
s=list(map(int,input().split()))
print(separation(n,s))