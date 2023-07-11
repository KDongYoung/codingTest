'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

1. push X: 정수 X를 큐에 넣는 연산이다.
2. pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
3. size: 큐에 들어있는 정수의 개수를 출력한다.
4. empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
5. front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
6. back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
q=deque()
# popleft, appendelft
# insert, remove
# extendleft


# [끝 ----- 시작] -> 이런 느낌으로 구성

for _ in range(n):
    line=sys.stdin.readline().rstrip().split()
    
    if len(line)==2 and line[0]=='push':
        q.appendleft(int(line[1])) 
    elif line[0]=="pop":
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif line[0]=="size":
        print(len(q))
    elif line[0]=="empty":
        if not q:
            print(1)
        else:
            print(0)
    elif line[0]=="front":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif line[0]=="back":
        if not q:
            print(-1)
        else:
            print(q[0])
    