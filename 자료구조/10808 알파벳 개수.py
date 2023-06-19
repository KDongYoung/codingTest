# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

# 런타임에러 : 간단한 계산은 숫자로 입력하기
word=input()
l=[0]*(122-97-1) # ord('z')-ord('a')-1

for w in word:
    l[ord(w)-97]+=1

print(*l) # asterisk : unpacking
