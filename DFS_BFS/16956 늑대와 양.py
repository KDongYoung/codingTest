'''
크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 
각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 
늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.

목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 
늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.
'''

# bfs

import sys
# sys.setrecursionlimit(20000) # 입력, 재귀 문제에서는 항상 작성 (시간제한 1초)

input=sys.stdin.readline

r,c=list(map(int, input().split()))

graph=[list(input().rstrip()) for _ in range(r)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

boolean=False

for i in range(r):
    for j in range(c):
        if graph[i][j]=='W':
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                
                if (0<=nx<r) and (0<=ny<c) and graph[nx][ny]=='S':
                    boolean=True
                    break
                
        elif graph[i][j]=='.':
            graph[i][j]='D'
        
if boolean:
    print(0)
else:
    print(1)
    for k in graph:
        print("".join(k))