'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
''' 

import sys

n,m,v=list(map(int, sys.stdin.readline().rstrip().split()))

graph=[[] for _ in range(n)]

for _ in range(m):
    a,b=list(map(int, sys.stdin.readline().rstrip().split()))
    
    graph[a-1].append(b)
    graph[b-1].append(a)    

for i in range(n):
    graph[i].sort()

### bfs 앞에서
visit_bfs=[]
queue=[v]

while queue:
    node=queue.pop(0)
    
    if node not in visit_bfs:
        visit_bfs.append(node)
        queue.extend(graph[node-1])
    

## dfs 뒤에서
visit_dfs=[]

def dfs(v):
    visit_dfs.append(v)    
    
    for i in graph[v-1]:
        if i not in visit_dfs:
            dfs(i)

dfs(v)

print(" ".join(map(str,visit_dfs)))
print(" ".join(map(str,visit_bfs)))