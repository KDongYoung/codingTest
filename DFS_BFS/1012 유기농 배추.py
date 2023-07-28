'''
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 
배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
'''

## -> DFS

import sys
sys.setrecursionlimit(10000) # 입력, 재귀 문제에서는 항상 작성 (시간제한 1초)

def dfs(x,y):
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if (0<=mx<m) and (0<=my<n):
                if graph[mx][my]==1:
                    graph[mx][my] = 0
                    dfs(mx, my)
                    
for _ in range(int(sys.stdin.readline())):
    m,n,k=list(map(int,sys.stdin.readline().split()))
    graph=[[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        i,j = list(map(int,sys.stdin.readline().split()))
        graph[i][j]=1

    count=0
    for x in range(m):
        for y in range(n):
            if graph[x][y]==1:
                dfs(x,y)
                count+=1

    print(count)