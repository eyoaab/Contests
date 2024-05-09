def calculate_lcp(s):
    n = len(s)
    lcp = [0] * n
    for i in range(1, n):
        j = lcp[i - 1]
        while j > 0 and s[i] != s[j]:
            j = lcp[j - 1]
        if s[i] == s[j]:
            j += 1
        lcp[i] = j
    return lcp

def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, l, r = map(int, input().split())  # Length of the string and the given range
        s = input().strip()  # The string
        lcp = calculate_lcp(s)
        print(lcp[l - 1])

if __name__ == "__main__":
    main()
