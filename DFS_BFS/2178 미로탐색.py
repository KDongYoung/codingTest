'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
# BFS

import sys
from collections import deque

input=sys.stdin.readline

n,m = list(map(int, input().rstrip().split()))

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

q=deque([(0,0)])

dx=[1,-1,0,0]
dy=[0,0,1,-1]

while q:
    x,y=q.popleft()
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny]==1:
            q.append((nx,ny))
            graph[nx][ny]=graph[x][y]+1 # 이전 가지까지 횟수 + 1

print(graph[n-1][m-1])
            