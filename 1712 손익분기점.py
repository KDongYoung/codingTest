import sys

a, b, c = list(map(int, sys.stdin.readline().split()))

if b>=c:
    print(-1)
else:
    print(int(a/(c-b))+1)       