from heapq import *
for _ in range(int(input())):
    n = int(input())
    peaple= list(map(int,input().split()))
    heap =[]

    for inx,val in enumerate(peaple):
        heap.append((-val,inx+1))
    heapify(heap)    

    answer = []
    while len(heap) > 1:
        person1 = heappop(heap)
        person2 = heappop(heap)
        if -person1[0] > 0 and -person2[0] > 0:
            answer.append([person1[1],person2[1]])

            heappush(heap,(person1[0]+1,person1[1])) 
            heappush(heap,(person2[0]+1,person2[1]))     
    print(len(answer))
    for i,j in answer:
        print(i,j)    




