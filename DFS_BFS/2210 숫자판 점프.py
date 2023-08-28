'''
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 
각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 
이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
'''
# dfs
import sys
input=sys.stdin.readline

graph=[input().rstrip().split() for _ in range(5)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=[]

def dfs(i,j, s):
    
    if len(s)==6: # 6자리 완성
        result.append(s)
        return
        
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        
        if (0<=nx<5) and (0<=ny<5):
            dfs(nx, ny, s+graph[nx][ny])
               

for i in range(5):
    for j in range(5): 
        dfs(i,j, graph[i][j])
                
print(len(set(result)))
                    
                