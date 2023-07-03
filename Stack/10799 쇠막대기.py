
import sys

words=sys.stdin.readline()

stack=[]
ans=0
for i in range(len(words)):
    if words[i]=="(":
        stack.append(words[i])
    elif words[i]==")":
        if words[i-1]=="(":
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1
            
print(ans)