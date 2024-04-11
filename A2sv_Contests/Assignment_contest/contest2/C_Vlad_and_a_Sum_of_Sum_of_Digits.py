def sum_of_digits(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total

def sum_of_numbers(n):
    digit_sum = 0
    for i in range(1, 10):
        repeat_count = (n - i) // 9 + 1
        digit_sum += i * repeat_count
    return digit_sum

t = int(input())
for _ in range(t):
    n = int(input())
    total_sum = sum_of_numbers(n)
    print(total_sum)
