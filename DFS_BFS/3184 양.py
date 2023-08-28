'''
미키의 뒷마당에는 특정 수의 양이 있다. 그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.

마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.

한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 
마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 
그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.

아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.
'''

import sys
from collections import deque

input=sys.stdin.readline

r,c=list(map(int, input().rstrip().split()))

graph=[list(input().rstrip()) for _ in range(r)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    
    s=0
    w=0
    
    q=deque([[x,y]])
    
    if graph[x][y]=="v":
        w+=1
    elif graph[x][y]=="o":
        s+=1
    
    graph[x][y]="#"
    
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx<r) and (0<=ny<c) and graph[nx][ny]!="#":
                if graph[nx][ny]=="v":
                    w+=1
                elif graph[nx][ny]=="o":
                    s+=1
                
                graph[nx][ny]="#"
                q.append([nx,ny])
    return s,w

total=[0,0] # sheep, wolf

for i in range(r):
    for j in range(c):
        if graph[i][j] in "ov": # sheep, wolf만
            s, w = bfs(i,j)
            
            if s>w:
                total[0]+=s
            elif s<=w:
                total[1]+=w

print(total[0], total[1])