
words=list(input())

stack=[]
ans=0
temp=1

for i in range(len(words)):
    # 열린 괄호들
    if words[i]=='(':
        temp*=2
        stack.append('(')
    elif words[i]=='[':
        temp*=3
        stack.append('[')
        
    # 닫힌 괄호들
    elif words[i]==')':
        if not stack or stack[-1] == '[': # 없거나, 괄호가 다르면
            ans=0
            break
        elif words[i-1]=='(': # 괄호쌍
            ans+=temp
        # temp 초기화
        temp//=2
        stack.pop()
    elif words[i]==']':
        if not stack or stack[-1] == '(': # 없거나, 괄호가 다르면
            ans=0
            break
        elif words[i-1]=='[': # 괄호쌍
            ans+=temp
        # temp 초기화
        temp//=3
        stack.pop()
        
if stack: # 비어 있지 않은 경우
    ans=0       

print(ans)