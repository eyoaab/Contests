for _ in range(int(input())):
    name = input()
    if len(set(name)) == 1:
        print(-1)
    else:
        print(len(name)-1)
        # l=0
        # while name[r]==name[0] and r>=0:
        #     r-=1
        # if r<0:
        #     print(-1)    
        # else:
        #     print(r-l+1)        