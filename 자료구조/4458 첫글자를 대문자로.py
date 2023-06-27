# 문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.

n=int(input())

ls=[]

for _ in range(n):
    l=input()
    ls.append(l[0].upper()+l[1:])
    
for l in ls:
    print(l)