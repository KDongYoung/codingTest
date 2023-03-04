import sys

num=int(input())
a=[]

for i in range(num):
    a.append(str(sum(list(map(int, sys.stdin.readline().split())))))

print("\n".join(a))