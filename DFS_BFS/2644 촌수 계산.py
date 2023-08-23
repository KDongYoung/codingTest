'''
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
이러한 촌수는 다음과 같은 방식으로 계산된다. 
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 
아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
'''

import sys
sys.setrecursionlimit(10000)

# dfs
input=sys.stdin.readline

n=int(input())
a,b=list(map(int,input().rstrip().split()))
m=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=list(map(int,input().rstrip().split())) # x: 부모, y: 자식
    graph[x].append(y)
    graph[y].append(x)  

visited=[False for _ in range(n+1)]
flag=False
result=[]

def dfs(v, cnt):
    cnt+=1
    visited[v]=True
    
    if v==b:
        result.append(cnt)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)
            
dfs(a, 0)

if not len(result):
    print(-1)
else:     
    print(result[0]-1)