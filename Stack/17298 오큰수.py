'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 
NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
'''

import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
stack=[]
ans=[-1 for _ in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]]<arr[i]:
        ans[stack.pop()]=arr[i]
    stack.append(i) # 값이 아닌 index를 append하기

print(" ".join(map(str,ans)))

# 시간 초과
# for i in range(len(arr)):
#     stack.append(arr[i]) 
    
#     if i==len(arr)-1:
#         stack.pop()
#         stack.append(-1)
#         break
    
#     for j in range(i+1,len(arr)):
#         if stack[-1]<arr[j]:
#             stack.pop()
#             stack.append(arr[j])
#             break
        
#         if j==len(arr)-1:
#             stack.pop()
#             stack.append(-1)            

# print(" ".join(map(str,stack)))