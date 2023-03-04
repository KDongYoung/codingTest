import sys

n, x = list(map(int, sys.stdin.readline().split()))
l = list(sys.stdin.readline().split())
l2=l.copy()
      
# for i in range(n):
#     print(l[i])
#     if x<int(l[i]):
#         l2.remove(l[i])

# print(" ".join(l2))


for i in range(n):
    if x>int(l[i]):
        print(int(l[i]), end=" ")