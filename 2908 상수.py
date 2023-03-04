import sys

a,b=list(sys.stdin.readline().split())
a=[i for i in a]
b=[i for i in b]

temp=a[0]
a[0]=a[2]
a[2]=temp

temp=b[0]
b[0]=b[2]
b[2]=temp

print(max([int("".join(a)), int("".join(b))]))