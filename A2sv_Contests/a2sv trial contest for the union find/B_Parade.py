l = 0
r = 0
store = []
for i in range(int(input())):
    a,b = map(int,input().split())
    l+= a
    r+= b
    store.append([a,b])
for i,j in  store:
    l-=    