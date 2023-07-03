'''
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 
그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 
3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 
그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 
식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.
'''

import sys

num=int(sys.stdin.readline().rstrip())
eq=sys.stdin.readline().rstrip()

nls=[]
for _ in range(num):
    nls.append(int(sys.stdin.readline().rstrip()))

stack=[]

for w in eq:
    if 'A'<=w<='Z':
        stack.append(nls[ord(w)-ord('A')])
    else:
        s2=stack.pop()
        s1=stack.pop()
        
        # 결과 삽입
        if w=="+": 
            stack.append(s1+s2)
        elif w=="-":
            stack.append(s1-s2)
        elif w=="/":
            stack.append(s1/s2)
        elif w=="*":
            stack.append(s1*s2)

print('%.2f'%stack[0])