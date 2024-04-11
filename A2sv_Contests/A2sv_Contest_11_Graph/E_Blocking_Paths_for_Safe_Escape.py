def cheack(row,col,C,R,graph,visited):
    return 0<=row<R and 0<=col<C and graph[row][col] !='#' and (row,col) not in visited

for _ in range(int(input())):
    R,C = list(map(int,input().split()))
    graph = []
    for i in range(R):
        Row = input()
        graph.append(list(Row))

    bad ,good ,empty = [],[],[]
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='G':
                good.append((i,j))  
            if graph[i][j]=='B':
                bad.append((i,j))
            if graph[i][j]=='.':
                empty.append((i,j))

    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    for row,col in empty:
        for r,c in directions:
            new_row ,new_col = r+row, col+c
            if 0<= new_col <C and 0<= new_row <R and graph[new_row][new_col] == 'B':
                graph[row][col] = '#'
                break
        
    stack = [(R-1,C-1)]
    visited = set()
    while stack:
        row,col = stack.pop()
        if not cheack(row,col,C,R,graph,visited):
            continue
        visited.add((row,col))
        for r,c in directions:
            new_row,new_col = row+r , col+c
            stack.append((new_row,new_col))
         
    flag  = True
    for g_d in good:
        if g_d not in visited:
            flag = False
            break
  
    for b_d in bad:
        if b_d  in visited:
            flag = False
            break  
        
    if flag:
        print("Yes")    
    else:
        print("No")           
                


