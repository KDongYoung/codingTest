# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

import sys

k=int(sys.stdin.readline())

arr=[]

for _ in range(k):
    num=int(sys.stdin.readline())
    
    if num==0 and len(arr)!=0:
        arr.pop()
    else:
        arr.append(num)
        
print(sum(arr))
        