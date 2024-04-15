from collections import Counter
def count_good_subsegments(n, m, k, a, b):
    b_freq = Counter(b)
    window_freq = Counter(a[:m])
    good_subsegments = 0
    if sum((b_freq & window_freq).values()) >= k:
        good_subsegments += 1
    
    
    for i in range(1, n - m + 1):
       
        window_freq[a[i - 1]] -= 1
        if window_freq[a[i - 1]] == 0:
            del window_freq[a[i - 1]]
        
        
        window_freq[a[i + m - 1]] += 1
        
        
        if sum((b_freq & window_freq).values()) >= k:
            good_subsegments += 1
    
    return good_subsegments


t = int(input())


for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    
    result = count_good_subsegments(n, m, k, a, b)
    print(result)
