for _ in range(int(input())):
    num = int(input())
    if num  == 1:
        print(3)
    else:
        answer = 1
        while (num & answer) == 0:
            answer <<= 1# to find the last one
        cnt = 0

        while num != 0:
            cnt += num & 1
            num >>= 1

        if cnt == 1:
            print(answer +1)# if it is power of two
        else:
            print(answer)        