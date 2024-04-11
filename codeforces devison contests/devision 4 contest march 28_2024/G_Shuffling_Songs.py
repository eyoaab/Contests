# Function to count the minimum number of removals needed to make the playlist exciting
def count_removals(n, songs):
    removals = 0
    
    # Iterate through the playlist and count removals
    for i in range(n - 1):
        if songs[i][0] != songs[i + 1][0] and songs[i][1] != songs[i + 1][1]:
            removals += 1
    
    return removals

# Number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    songs = []
    
    # Read the songs
    for _ in range(n):
        gi, wi = input().split()
        songs.append((gi, wi))
    
    # Count the minimum number of removals needed
    removals = count_removals(n, songs)
    print(removals)
