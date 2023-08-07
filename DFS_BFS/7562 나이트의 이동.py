'''
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''

import sys
from collections import deque
sys.setrecursionlimit(10000) # 입력, 재귀 문제에서는 항상 작성 (시간제한 1초)

input = sys.stdin.readline
t = int(input())

dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]

for _ in range(t):
    
    l=int(input()) # 체스판의 한변의 길이
    graph=[[0 for _ in range(l)] for _ in range(l)]
    
    x,y=map(int,input().split()) # 나이트가 현재 있는 칸
    ex,ey=map(int,input().split()) # 나이트가 이동하려고 하는 칸
    
    # 시작점
    q=deque([(x,y)])
    graph[x][y]=1
    
    while q:
        x,y=q.popleft()
        
        if x==ex and y==ey:
            print(graph[x][y]-1)
            break
        
        for i in range(8):
            mx=x+dx[i]
            my=y+dy[i]
             
            if (0<=mx<l) and (0<=my<l) and not graph[mx][my]:
                graph[mx][my]=graph[x][y]+1 # 이전 위치에 +1 하기
                q.append((mx,my))
