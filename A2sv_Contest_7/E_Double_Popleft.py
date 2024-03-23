
li=list(map(int,input().split()))
n=li[0]
q=li[1]
input_li=list(map(int,input().split()))

ex=input_li
ref=dict()
for i in range(q):
    k=int(input())
    ref[k]=[]
if ref:
    ma=max(ref)
    for i in range(1,ma+1):
        a=ex.pop(0)
        b=ex.pop(0)
        
        if i in ref:
            ref[i].extend([a,b])
        if a>b:
            ex.insert(0,a)
            ex.append(b) 
        else:
            ex.insert(0,b)
            ex.append(a) 
    for i in ref:
        li=ref[i]
        print(* li)              