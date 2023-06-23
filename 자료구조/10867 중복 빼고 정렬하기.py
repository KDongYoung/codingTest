# N개의 정수가 주어진다. 
# 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 
# 같은 정수는 한 번만 출력한다.

n=int(input())

ls=list(map(int,input().split()))
ls=list(set(ls))
ls.sort()

for i in ls:
    print(i, end=" ")