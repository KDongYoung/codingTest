import sys
s=[]

while 1:
    a,b = list(map(int, sys.stdin.readline().split()))
    
    if a==0 and b==0:
        break
    else:
        s.append(str(a+b))

print("\n".join(s))