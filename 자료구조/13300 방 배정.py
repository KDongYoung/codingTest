# 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 
# 또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 물론 한 방에 한 명만 배정하는 것도 가능하다.
# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.

n,k=list(map(int, input().split()))

t=[[0,0] for _ in range(6)]
for i in range(n):
    a,b=list(map(int, input().split()))
    t[b-1][a]+=1


m=0
for i in range(6): # 학년
    for j in range(2): # 성별
        if t[i][j]!=0:
            if t[i][j]%k==0:
                m+=t[i][j]//k
            else: 
                m=m+t[i][j]//k+1

print(m)