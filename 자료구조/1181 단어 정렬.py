# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

n=int(input())

words=[]
ls=[[] for _ in range(50)]

for _ in range(n):
    words.append(input())

words=list(set(words))

for i in range(len(words)):
    ls[len(words[i])-1].extend([i])

ans=[]
for l in ls:
    if len(l)>1:
        ans.extend(sorted([words[i] for i in l]))
    elif len(l)==1:
        ans.append(words[l[0]])
        
for an in ans:
    print(an)