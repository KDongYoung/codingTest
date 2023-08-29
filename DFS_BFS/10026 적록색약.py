'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
'''

# 적록색약 r=g
import sys
input=sys.stdin.readline

n=int(input().rstrip())
graph=[list(input().rstrip()) for _ in range(n)]

visit=[[False for _ in range(n)] for _ in range(n)] 

dx=[0,0,1,-1]
dy=[1,-1,0,0]

from collections import deque

cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            q=deque([[i,j]])
            cnt+=1
            
            while q:
                x,y=q.popleft()
                visit[x][y]=True

                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    
                    if (0<=nx<n) and (0<=ny<n) and not visit[nx][ny]:
                        if graph[nx][ny]==graph[i][j]:
                            visit[nx][ny]=True
                            q.append([nx,ny])
        # print(cnt)                        
    



# 색약
for i in range(n):
    for j in range(n):
        if graph[i][j]=="R":
            graph[i][j]="G"
visit=[[False for _ in range(n)] for _ in range(n)] 

s_cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            q=deque([[i,j]])
            s_cnt+=1
            
            while q:
                x,y=q.popleft()
                visit[x][y]=True

                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    
                    if (0<=nx<n) and (0<=ny<n) and not visit[nx][ny]:
                        if graph[nx][ny]==graph[i][j]:
                            visit[nx][ny]=True
                            q.append([nx,ny])

print(cnt, s_cnt)