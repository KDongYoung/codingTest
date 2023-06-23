# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

n=int(input())

xys=[]
for _ in range(n):
    xys.append(list(map(int, input().split())))

xys=[[j,i] for i, j in xys]
xys.sort()

for xy in xys:
    xy.reverse()
    print(" ".join([str(i) for i in xy]))