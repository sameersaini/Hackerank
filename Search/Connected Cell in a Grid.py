def FindIndex(G,val):
    for row,l in enumerate(G):
        for col,x in enumerate(l):
            if x == val:
                return row,col

visited=set()
def BFS(G,i,j,m,n):
    q=[Grid[i][j]]
    visit=set()
    while(len(q)!=0):
        
        
        val=q.pop(0)

        
        i,j=FindIndex(Grid,val)
        
        if val not in visit:
            visit.add(val)
            visited.add(val)
        
        if i==m-1 and j==n-1:
            q=[]
            break
            
        if i==m-1:
            if Grid[i][j+1] != 0 and Grid[i][j+1] not in visit:
                q.append(Grid[i][j+1])
            continue
        
        if j==0:
            if Grid[i][j+1] != 0 and Grid[i][j+1] not in visit:
                q.append(Grid[i][j+1])
            if Grid[i+1][j+1] != 0 and Grid[i+1][j+1] not in visit:
                q.append(Grid[i+1][j+1])
            if Grid[i+1][j] != 0 and Grid[i+1][j] not in visit:
                q.append(Grid[i+1][j])
            continue
            
        if j==n-1:
            if Grid[i+1][j-1] != 0 and Grid[i+1][j-1] not in visit:
                q.append(Grid[i+1][j-1])
            if Grid[i+1][j] != 0 and Grid[i+1][j] not in visit:
                q.append(Grid[i+1][j])
            continue
        
        if i==0:
            if Grid[i][j+1] != 0 and Grid[i][j+1] not in visit:
                q.append(Grid[i][j+1])
            if Grid[i+1][j+1] != 0 and Grid[i+1][j+1] not in visit:
                q.append(Grid[i+1][j+1])
            if Grid[i+1][j] != 0 and Grid[i+1][j] not in visit:
                q.append(Grid[i+1][j])
            if Grid[i+1][j-1] != 0 and Grid[i+1][j-1] not in visit:
                q.append(Grid[i+1][j-1])
            if Grid[i][j-1] != 0 and Grid[i][j-1] not in visit:
                q.append(Grid[i][j-1])
            continue
        
        
        if Grid[i][j+1] != 0 and Grid[i][j+1] not in visit:
            q.append(Grid[i][j+1])
        if Grid[i+1][j+1] != 0 and Grid[i+1][j+1] not in visit:
            q.append(Grid[i+1][j+1])
        if Grid[i+1][j] != 0 and Grid[i+1][j] not in visit:
            q.append(Grid[i+1][j])
        if Grid[i+1][j-1] != 0 and Grid[i+1][j-1] not in visit:
            q.append(Grid[i+1][j-1])
        if Grid[i][j-1] != 0 and Grid[i][j-1] not in visit:
            q.append(Grid[i][j-1])
        if Grid[i-1][j] != 0 and Grid[i-1][j] not in visit:
            q.append(Grid[i-1][j])
        if Grid[i-1][j+1] != 0 and Grid[i-1][j+1] not in visit:
            q.append(Grid[i-1][j+1])
    return(len(visit))

m=int(input())
n=int(input())
Grid=[list(map(int,input().split())) for _ in range(m)]


count=1
Max=1
for i in range(m):
    for j in range(n):
        if Grid[i][j]==1:
            Grid[i][j]=count
            count += 1


    
for i in range(m):
    for j in range(n):
        if Grid[i][j] != 0 and Grid[i][j] not in visited:
            length=BFS(Grid,i,j,m,n)
            
            if length > Max:
                Max=length
                    

print(Max)