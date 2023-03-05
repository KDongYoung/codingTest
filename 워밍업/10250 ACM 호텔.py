import sys

test_num=int(input())
ans=[]

for i in range(test_num):
    h,w,n = list(map(int, sys.stdin.readline().split()))
    
    if n%h==0:
        ans.append(str(n//h+h*100))
    else:
        ans.append(str(n//h+n%h*100+1))
    
print("\n".join(ans))

