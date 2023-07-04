n=int(input())

stack=[]
for i in range(n):
    w,h=map(int, input().split())
    stack.append([w,h])
       
stack.sort()

# 가장 높은 기둥의 index
m_h=0
idx=0
for i,l in enumerate(stack):
    if m_h<l[1]:
        m_h=l[1]
        idx=i
ans=0

# 앞에서부터 비교
height=stack[0][1]
for j in range(idx):
    ans+=height*(stack[j+1][0]-stack[j][0])
    if height<stack[j+1][1]:
        height=stack[j+1][1]
        
# 가장 높은 기둥
ans+=height

# 뒤에서부터 비교
height=stack[-1][1]
for j in range(n-1, idx, -1):
    ans+=height*(stack[j][0]-stack[j-1][0])
    if height<stack[j-1][1]:
        height=stack[j-1][1]
    
print(ans)   