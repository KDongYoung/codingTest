'''
키보드가 잘못 눌려서 보고서의 모든 글자가 A와 B로 바뀌어 버렸다! 
그래서 평석이는 보고서 작성을 때려치우고 보고서에서 '좋은 단어'나 세보기로 마음 먹었다.

평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다. 
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 
짝 지을수 있다면, 그 단어는 '좋은 단어'이다. 평석이가 '좋은 단어' 개수를 세는 것을 도와주자.
'''

import sys

n=int(sys.stdin.readline())

ans=0

for i in range(n):
    words=list(sys.stdin.readline().rstrip())
    stack=[words[0]]
    for j in range(1,len(words)):
        if not stack:
            stack.append(words[j])
        elif words[j]==stack[-1]:
            stack.pop()
        else:
            stack.append(words[j])
    
    if not stack:
        ans+=1

print(ans)
