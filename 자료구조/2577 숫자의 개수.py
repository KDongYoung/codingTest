# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a=int(input())
b=int(input())
c=int(input())

num=a*b*c
a=[0,0,0,0,0,0,0,0,0,0]

while num!=0:
    a[num%10]+=1
    num=num//10
    
for i in a:
    print(i)