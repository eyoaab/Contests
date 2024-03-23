import math

def find_road_position(n, preferences):
    # Count the number of zeros and ones
    zeros_count = preferences.count('0')
    ones_count = n - zeros_count

    # Initialize cumulative counts
    cumulative_zeros = 0
    cumulative_ones = 0

    min_difference = math.inf
    road_position = -1

    # Iterate through preferences and find optimal road position
    for i in range(n - 1):
        if preferences[i] == '0':
            cumulative_zeros += 1
        else:
            cumulative_ones += 1

        # Calculate number of zeros to the left and ones to the right
        zeros_left = cumulative_zeros
        ones_right = ones_count - cumulative_ones

        # Check if at least half of the residents on each side are satisfied
        if zeros_left >= math.ceil(n / 2) and ones_right >= math.ceil(n / 2):
            # Update road position if closer to the middle
            difference = abs(n // 2 - i)
            if difference < min_difference:
                min_difference = difference
                road_position = i + 1

    return road_position

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    preferences = input().strip()
    road_position = find_road_position(n, preferences)
    print(road_position)
