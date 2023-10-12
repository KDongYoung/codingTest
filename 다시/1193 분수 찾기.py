'''
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 
차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오
'''

num=int(input())
cnt=1

while num>cnt:
    num-=cnt
    cnt+=1

if cnt%2==0:
    a=num
    b=cnt-num+1
else:
    a=cnt-num+1
    b=num

print(f'{a}/{b}')