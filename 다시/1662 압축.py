'''
압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. 
K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 이 Q라는 문자열이 K번 반복된다는 뜻이다. 
압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.
'''

import sys

input=sys.stdin.readline

line=input()

stack=[]
num=0

for i in range(len(line)):
    
    if line[i]!='(' and line[i]!=')':
        num+=1
    
    elif line[i]=='(':
        stack.append([num-1, int(line[i-1])])
        num=0
    elif line[i]==')':
        if not stack:
            break
        else: 
            n=stack.pop()
            num=num*n[1]+n[0]
print(num-1)
