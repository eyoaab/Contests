from heapq import *
for _ in range(int(input())):
    n  = int(input())
    final = n
    nums = list(map(int,input().split()))

    max_h = []
    for i,j in enumerate(nums):
        heappush(max_h,[-j,i])

    ans = []
    visited = set()
    while True:
        if not max_h or len(ans) == n:
            break
        val,index = heappop(max_h)
        if index >= final:  
            continue
        for i in range(index,final):
            ans.append(nums[i])
        # print(index)
        final = index
    print(*ans)      
















# x=int(input())
# z=[]

# def display(x):
#     for j in x:
#         print(j,end=' ')
#     print()

# # def sort_d(a):
# #     if(a==sorted(a)

# for i in range(x):
#     a=int(input())
#     z.append(list(map(int,input().split())))
# for i in z:
#     if(i==sorted(i)):
#         display(i[::-1])
#     elif(i[::-1]==sorted(i)):
#         display(i)
#     else:
#         ts=[]
#         while(len(i)!=0):
#             o=i.index(max(i))
#             ts=ts+i[o:]
#             i=i[:o]
#         display(ts)

