x=int(input())
max_n=0
for i in range(x,0,-1):
    if(i==1):
        max_n+=1.0
    
    else:
        max_n+=(1)/i
print('%.12f'%max_n)
