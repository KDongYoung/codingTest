import sys

student=int(input())
result=[]

for i in range(student):
    s=list(map(int, sys.stdin.readline().split()))
    result.append(f'%.3f'%(sum([s[i]>sum(s[1:])//s[0] for i in range(1,s[0]+1)])/s[0]*100)+"%")

print("\n".join(result))
