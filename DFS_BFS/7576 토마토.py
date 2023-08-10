'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
# DFS

import sys
from collections import deque

input=sys.stdin.readline

m,n=list(map(int, input().rstrip().split()))

graph=[list(map(int, input().rstrip().split())) for _ in range(n)]
q=deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y=q.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny]==0:
            graph[nx][ny] = graph[x][y]+1
            q.append((nx,ny))
    
flag=False
for i in graph:
    if 0 in i:
        flag=True
        break

if flag:
    print(-1)
else:
    print(max(map(max,graph))-1) # 처음 시작을 1로 표현했으니 1을 빼준다.
