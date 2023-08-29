'''
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, 
i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
'''
# 그래프 최단 거리

import sys
input=sys.stdin.readline

n=int(input())

graph=[list(map(int, input().rstrip().split())) for _ in range(n)]

# i -> k -> j
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for g in graph:
    for gi in g:
        print(gi, end=" ")
    print()
