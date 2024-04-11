import math

# Function to check if a number is a binary decimal
def is_binary_decimal(num):
    while num % 2 == 0:
        num //= 2
    return num == 1

# Function to check if n can be represented as a product of binary decimals
def can_be_product_of_binary_decimals(n):
    # Special case: 1 is already a binary decimal
    if n == 1:
        return True
    
    # Iterate through possible divisors up to sqrt(n)
    for i in range(2, int(n)):
        if n % i == 0:
            # Check if both the divisor and quotient are binary decimals
            if is_binary_decimal(i) and is_binary_decimal(n // i):
                return True
    return False

# Number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    if can_be_product_of_binary_decimals(n):
        print("YES")
    else:
        print("NO")
