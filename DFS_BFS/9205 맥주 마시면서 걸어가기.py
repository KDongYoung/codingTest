'''
송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 
올해는 맥주를 마시면서 걸어가기로 했다. 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 
맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 
즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.

상근이의 집에서 페스티벌이 열리는 곳은 매우 먼 거리이다. 따라서, 맥주를 더 구매해야 할 수도 있다. 
미리 인터넷으로 조사를 해보니 다행히도 맥주를 파는 편의점이 있다. 
편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 
하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 
편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 
상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.
'''
import sys
from collections import deque

input=sys.stdin.readline

t=int(input().rstrip())

for _ in range(t):
    n=int(input().rstrip())
    
    s_x, s_y=map(int,input().rstrip().split())
    c_xy=[list(map(int,input().rstrip().split())) for _ in range(n)]    
    e_x, e_y=map(int,input().rstrip().split())
      
    visited=[False for _ in range(n+1)] # c_xy랑 festival
    
    
    q=deque([[s_x,s_y]])
    flag=False
    
    # 거리 1000 (50m*20개)
    while q:
        
        x,y=q.popleft()
        
        if abs(e_x-x) + abs(e_y-y)<=1000:
            print("happy")
            flag=True
            break
        
        # 편의점 도달 시
        for i in range(n):
            if not visited[i]:
                new_x, new_y=c_xy[i]
                
                if abs(new_x-x) + abs(new_y-y)<=1000:
                    q.append([new_x,new_y])
                    visited[i]=True
                    
    if not flag:
        print('sad')