# N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램을 작성하시오.

import sys

n=int(sys.stdin.readline())

ans=[]
for _ in range(n):
    ans.append(int(sys.stdin.readline()))

ans.sort(reverse=True)

for an in ans:
    print(an)