# Function to check if a given substring satisfies the conditions
def check_substring(s, k):
    # Initialize the number of different characters
    diff_chars = 0
    
    # Iterate through the string and count different characters
    for i in range(len(s)):
        if s[i] != k[i % len(k)]:
            diff_chars += 1
            if diff_chars > 1:
                return False
    
    return True

# Function to find the length of the shortest repeating substring
def shortest_repeating_substring(s):
    # Iterate over possible lengths of substrings
    for length in range(1, len(s) + 1):
        k = s[:length]
        if check_substring(s, k):
            return length
    
    return len(s)

# Number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    # Find the length of the shortest repeating substring
    result = shortest_repeating_substring(s)
    print(result)
