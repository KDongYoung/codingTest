# N개의 수가 주어졌을 때, 이를 비내림차순으로 정렬하는 프로그램을 작성하시오.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import sys

n=int(sys.stdin.readline())

ans=[]
for _ in range(n):
    ans.append(int(sys.stdin.readline()))

ans.sort()

for an in ans:
    print(an)