s=list(map(int,input().split()))
s.sort()
key=int(input())
l,h=0,len(s)-1
def binary_search(s,key,l,h):
    mid=(l+h)//2
    while l<h:
        if key==s[mid]:   
            print("element",key,"is found at index",mid)  
            break
            # h=mid-1
        if key>s[mid]:
            l=mid+1
        if key<s[mid]:
            h=mid-1
    else:
        print("key element not found")
binary_search(s,key,l,h)
            
            #1 2 3 4 5 6
            
    