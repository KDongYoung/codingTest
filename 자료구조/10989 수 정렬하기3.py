# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 메모리

import sys

n=int(sys.stdin.readline())

ls=[0]*10001 # input 값을 index로 접근

for _ in range(n):
    ls[int(sys.stdin.readline())]+=1 # runtime을 줄이기 위한

# ls.sort() # 메모리 사용 큼
for i in range(len(ls)):
    if ls[i]!=0:
        for _ in range(ls[i]): # 여러번 입력된 숫자는 여러번 출력
            print(i)