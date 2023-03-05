t=int(input())
ans=[]

for _ in range(t):
    k=int(input())
    n=int(input())
    f=list(range(1,n+1))
    for i in range(k):
        for j in range(1,n):
            f[j]+=f[j-1]
    
    print(f[n-1])      