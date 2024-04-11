def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)
def merge(left,right):
    global answer
    result = []
    if left[0]<right[0]:
        result.extend(left+right)
    else:
        result.extend(right+left)
        answer +=1
    return result

for _ in range(int(input())):
    answer = 0  
    n = int(input())
    nums = list(map(int,input().split()))
    if merge_sort(nums) == sorted(nums):
        print(answer)
    else:
        print(-1)         


