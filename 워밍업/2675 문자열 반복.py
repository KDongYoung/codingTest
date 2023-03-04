import sys

num=int(input())
b=""

for i in range(num):
    a, l = list(map(str, sys.stdin.readline().split()))
    for i in range(len(l)):
        b+=l[i]*int(a)
    b+="\n"
print(b)    