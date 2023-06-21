# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n=int(input())

ls=[]
for _ in range(n):
    ls.append(int(input()))

ls=sorted(ls)
for l in ls:
    print(l)