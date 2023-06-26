# 기타를 시리얼 번호 순서대로 정렬하고자 한다.
# 모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.
# 시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.
# 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
# 시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

n=int(input())
ls=[]

def sum_num(inputs):
    num=0
    for x in inputs:
        if x.isdigit(): # x가 숫자인지 확인
            num+=int(x)
    return num

for j in range(n):
    ls.append(input())

ls.sort(key=lambda a: (len(a), sum_num(a), a)) 
# key를 괄호로 순차적으로 입력하면 해당 순서로 정렬됨

for l in ls:
    print(l)
