'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 
자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.
'''
# 1부터 차근차근 숫자가 나열된다. -> 1-> append -> 2 -> append -> ...
# 입력된 수가 4이면 4번 append하고 1번 pop, 그다음이 3이면 또 pop -> 진행
# 입력한 수열을 만들어가는 것

import sys
input=sys.stdin.readline

n=int(input())
arr=[]
ans=[]
flag=False
current=1

for i in range(n):
    num=int(input().rstrip())
    
    while current<=num:
        arr.append(current)
        ans.append("+")
        current+=1
    
    if arr[-1]==num: # 입력된 수와 동일한 수 도착
        arr.pop()
        ans.append("-")
    else:
        print("NO")
        flag=True
        break
    
if not flag:
    for i in ans:   
        print(i)
