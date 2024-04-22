
def inbound(row,col):
    return 0<= row < 2 and 0<=col<n
def dfs(row,col):
    #print(row,col) 

    if row == 1 and col == n-1:
        return True
    if (row,col) in visited:
        return False
    visited.add((row,col)) 
    x = False
    y = False   
    z = False
    #print(row,col)
    if inbound(row,col+1) and grid[row][col+1] == grid[row][col]:
       x= dfs(row,col+1)
    if inbound(row+1,col) and grid[row+1][col] != grid[row][col]:
        y=dfs(row+1,col)
    if inbound(row-1,col) and grid[row-1][col] != grid[row][col]:
        z=dfs(row-1,col)    
    return x or y or z     
      

for _ in range(int(input())):
    visited =set()
    n = int(input())
    grid = []
    for j in range(2):
        grid.append(input())
    # print(grid)    
    if dfs(0,0):
        print("NO")
    else:
        print("YES")    

