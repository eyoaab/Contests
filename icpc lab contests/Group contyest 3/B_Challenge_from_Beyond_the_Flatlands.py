A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
AB = (B[0] - A[0], B[1] - A[1])
AC = (C[0] - A[0], C[1] - A[1])

ans = AB[0] * AC[1] - AB[1] * AC[0]

if ans > 0:
    print("LEFT")
elif ans < 0:
    print("RIGHT")
else:
    print("TOWARDS")
