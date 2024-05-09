from collections import defaultdict, deque
def check(num,k):
    return num & (1 << k) != 0

n, k = map(int, input().split())
ans = defaultdict(int)
q = deque()
for i in range(31):
    if check(n,i):
        if i > 0:
            q.append(1 << i)
        ans[1 << i] += 1

if len(ans) > k:
    print("NO")
    exit()

cnt = len(ans)
while cnt < k and q:
    z = q.popleft()
    ans[z] -= 1
    ans[z // 2] += 2
    if z // 2 > 1:
        q.append(z // 2)
        q.append(z // 2)
    cnt += 1

if cnt < k:
    print("NO")
else:
    print("YES")
    answer = []
    for i,j in ans.items():
        for k in range(j):
            answer.append(i)

    print(*answer)        
