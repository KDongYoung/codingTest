# 문자열 N개가 주어진다. 
# 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

import sys

while True:
    ss=sys.stdin.readline().rstrip("\n") # \n 제거
    
    if not ss: # 아무거도 입력 안했을 때를 위한 break
        break

    # 소문자, 대문자, 숫자, 공백의 개수
    l,u,d,sp=0,0,0,0
    for s in ss:
        if s.isdigit():
            d+=1
        elif s.islower():
            l+=1
        elif s.isupper():
            u+=1
        elif s.isspace():
            sp+=1
    print(l, u, d, sp)