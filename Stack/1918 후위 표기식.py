'''
후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다. 
이 방법의 장점은 다음과 같다. 우리가 흔히 쓰는 중위 표기식 같은 경우에는 
덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만 후위 표기식을 
사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다. 
또한 같은 방법으로 괄호 등도 필요 없게 된다. 
예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오.
'''

eq=list(input())
stack=[]
result=''

for a in eq:
    if a.isalpha():
        result+=a
    # 우선 순위 순서대로 코딩
    elif a=='(':
        stack.append(a)
    elif a=='*' or a=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            result+=stack.pop()
        stack.append(a)
    elif a=='+' or a=='-':
        while stack and stack[-1]!='(':
            result+=stack.pop()
        stack.append(a)
    elif a==")":
        while stack and stack[-1]!='(':
            result+=stack.pop()
        stack.pop()
            
while stack:
    result+=stack.pop()
    
print(result)