# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

n=int(input())

ans=[]

for _ in range(n):
    ans.append(input().split())
    
ans.sort(key=lambda age:int(age[0])) # age에 따라만 sorting

for a,b in ans:
    print(a,b)