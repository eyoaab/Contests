for _ in range(int(input())):
    a,b,l = list(map(int,input().split()))
    i = 0
    a_ =[]
    b_=[]
    for i in range(l):
        if pow(a,i)>l:
            break
        a_.append(pow(a,i))
    for i in range(l):
        if pow(b,i)>l:
            break
        b_.append(pow(b,i))
    # print(a_)    
    answer = set()
    for i in range(len(a_)):
        for j in range(len(b_)):
            nums1 = a_[i]
            nums2 = b_[j]
            if l%(nums1*nums2)==0:
                k =(nums1*nums2)
                answer.add(l/k)
    print(len(answer))            


