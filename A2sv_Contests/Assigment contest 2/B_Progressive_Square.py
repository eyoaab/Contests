for _ in range(int(input())):
    n,c,d = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    matrix = []
    a = min(nums)
    row =[a]
    for i in range(n-1):
        row.append(row[-1]+ d)
    answer = []
    answer.extend(row)

    for i in range(n-1):
        temp = [i + c for i in row]
        answer.extend(temp)
        row = temp
     
    if sorted(answer) == sorted(nums):
        print("YES")
    else:
        print("NO")    
