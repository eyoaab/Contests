import math

# Function to find the minimum height of the tree
def min_tree_height(a, b, c):
    # Total number of vertices
    total_vertices = a + b + c
    
    # If a or b is zero, it means that we have a chain of vertices
    if a == 0 or b == 0:
        return total_vertices - 1
    
    # If c is greater than 1, it's not possible to create a tree
    if c > 1:
        return -1
    
    # Calculate the minimum height based on the number of vertices
    min_height = math.ceil(math.log2(total_vertices - b + 1))
    
    return min_height

# Number of test cases
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Find the minimum height of the tree
    result = min_tree_height(a, b, c)
    print(result)
