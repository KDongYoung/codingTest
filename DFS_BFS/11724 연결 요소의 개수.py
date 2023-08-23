'''
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
'''
# dfs
import sys
sys.setrecursionlimit(30000) # 입력, 재귀 문제에서는 항상 작성 (시간제한 1초)

input=sys.stdin.readline
n,m=list(map(int, input().split()))

graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v=list(map(int,input().split()))
    graph[u].append(v)
    graph[v].append(u)
        
visited=[False for _ in range(n+1)]
cnt=0

def dfs(u):
    visited[u]=True
    
    for i in graph[u]:
        if not visited[i]:
            visited[i]=True
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)
        
print(cnt)