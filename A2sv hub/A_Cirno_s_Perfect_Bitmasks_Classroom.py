for _ in range(int(input())):
    num = int(input())
    for i in range(1,2**30):
        if num ^ i and i & num:
            print(i)
            break