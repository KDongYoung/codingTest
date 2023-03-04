s=input().upper()
unique_word=list(set(s))
cnt=[]

for x in unique_word:
    cnt.append(s.count(x))

if cnt.count(max(cnt))>1:
    print("?")
else:
    print(unique_word[cnt.index(max(cnt))])