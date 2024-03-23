s=input()
new_str=[]
i=0
flag=False
for j in s:
    if new_str:
        if new_str[-1]==j:
            flag=True
        else:
            new_str.append(j) 
    else:
        new_str.append(j) 
    if flag:
        new_str.pop()
        flag=False
print(''.join(new_str))



"""
while i<len(s):
    if i<len(s)-1 and s[i]==s[i+1]:
        i+=2
    else:
        if new_str and s[i]==new_str[-1]:
            i+=1
            new_str=new_str[:-1] 
        else:
            new_str+=s[i]
            i=i+1
print(new_str)
 """                  
            
    
    