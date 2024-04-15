def can_make_equal(n, containers):
    target = sum(containers) // n

    for water in containers:
        if water != target:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    containers = list(map(int, input().split()))

    print(can_make_equal(n, containers))
