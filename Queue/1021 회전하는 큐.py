'''
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 
지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. : 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. : a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. : a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
'''

from collections import deque
import sys

n,m=list(map(int,sys.stdin.readline().split()))
q=deque(list(range(1,n+1)))
want=list(map(int,sys.stdin.readline().split()))

cnt=0
for w in want:
    while True:
        if q[0]==w:
            q.popleft()
            break
        else:
            if q.index(w)<len(q)/2:
            # 뽑아내려는 수의 위치 인덱스가 
            # q의 길이를 반으로 나눈것보다 작을때는 왼쪽으로
                while q[0]!=w:
                    q.append(q.popleft())
                    cnt+=1
            else:
            # 뽑아내려는 수의 위치 인덱스가 
            # q의 길이를 반으로 나눈것보다 클때는 오른쪽으로
                while q[0]!=w:
                    q.appendleft(q.pop())
                    cnt+=1
        
print(cnt)
