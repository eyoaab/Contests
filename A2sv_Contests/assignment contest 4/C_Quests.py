
def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

for _ in range(read_int()):
    n, k = read_int_list()
    a = read_int_list()
    b = read_int_list()
    res, sum_, mx = 0, 0, 0
    for i in range(min(n, k)):
        sum_ += a[i]
        mx = max(mx,b[i])
        res = max(res, sum_ + mx * (k - i - 1))
    print(res)

