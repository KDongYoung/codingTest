# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys

n=int(input())

ls=[]
for _ in range(n):
    ls.append(int(sys.stdin.readline())) # runtime을 줄이기 위한

ls.sort()
for l in ls:
    print(l)