def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != a[1]:
        print("YES")
    elif n == 2:
        print("NO")
    else:
        for i in range(1, n):
            if a[i] % a[0] != 0:
                print("YES")
                return
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
