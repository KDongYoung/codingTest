'''
정수를 저장하는 덱(Deque)를 구현한 다음, 
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

1. push_front X: 정수 X를 덱의 앞에 넣는다.
2. push_back X: 정수 X를 덱의 뒤에 넣는다.
3. pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
              만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
4. pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
             만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
5. size: 덱에 들어있는 정수의 개수를 출력한다.
6. empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
7. front: 덱의 가장 앞에 있는 정수를 출력한다. 
          만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
8. back: 덱의 가장 뒤에 있는 정수를 출력한다. 
         만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque
import sys

n=int(sys.stdin.readline())
q=deque([])

for _ in range(n):
    m=sys.stdin.readline().split()
    
    if m[0]=='push_back':
        q.append(int(m[1]))
    elif m[0]=='push_front':
        q.appendleft(int(m[1]))
    elif m[0]=='pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif m[0]=='pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif m[0]=='size':
        print(len(q))
    elif m[0]=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif m[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)        
    elif m[0]=='back':
        if q:
            print(q[-1])
        else:
            print(-1)