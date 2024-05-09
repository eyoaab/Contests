num = int(input())
answer = 0
while num > 0:
    answer += num & 1
    num = num >> 1
print(answer)    
