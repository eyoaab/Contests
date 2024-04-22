from heapq import heappush, heappop

answer = []
heap = []

def solve(command):
    key = command[0]
    if len(command) == 2:
        num = int(command[1])
    
    if key == 'insert':
        answer.append('insert ' + str(num))
        heappush(heap, num)
    elif key == 'removeMin':
        if heap:
            heappop(heap)
            answer.append('removeMin')
        else:
            answer.append('insert 0')
            answer.append('removeMin')
    else: 
        if heap:
            if heap[0] == num:
                answer.append('getMin ' + str(num))

            elif heap[0] < num:
                while heap and heap[0] < num:
                    heappop(heap)
                    answer.append('removeMin')
                if heap:
                    if heap[0] == num:
                        answer.append('getMin ' + str(num))
                    else:
                        heappush(heap,num) 
                        answer.append('insert ' + str(num))
                        answer.append('getMin ' + str(num))
                else:
                    heappush(heap,num) 
                    answer.append('insert ' + str(num))
                    answer.append('getMin ' + str(num))
                       
            else:
                heappush(heap,num) 
                answer.append('insert ' + str(num))
                answer.append('getMin ' + str(num))
        else:
            answer.append('insert ' + str(num))
            answer.append('getMin ' + str(num))
            heappush(heap, num)

n = int(input())

for _ in range(n):
    command = input().split()
    solve(command)

print(len(answer))
for ans in answer:
    print(ans)
