t=int(input())
for _ in range(t):
    n,m,x=list(map(int,input().split()))
    answer=set()
    temp=[x]
    for i in range(m):
        next_level=[]
        val,dir=list(input().split())
        val=int(val)
       
        for j in range(len(temp)):
          
            if dir=='?':
                val1=temp[j]-val
                if val1<=0:
                    val1=n-val1
                next_level.append(val1)
                val2=val+temp[j] 
                if val2!=n:
                    val2=val2%n 
                next_level.append(val2)  
            elif dir=='0':
                val2=val+temp[j]
                if val2!=n:
                    val2=val2%n 
                next_level.append(val2)
                answer.add(val2)
            elif dir=='1':
                val1=temp[j]-val
                if val1<=0:
                    val1=n-val1
                next_level.append(val1)
                answer.add(val1)
            else:
                print("noooooooooooooooooo")    
            

        
        temp=next_level
        
    print(len(answer))
    print(* list(answer))    
          


    
