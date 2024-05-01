refer = {}
for _ in range(int(input())):
    first,second = input().split()
    if first in refer:
        val = refer[first]
        del refer[first]
        refer[second] = val
    else:
        refer[second] = first  
print(len(refer))          
for i,j in refer.items():
    print(j,i)        