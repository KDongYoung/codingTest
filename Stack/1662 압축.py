# 압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 
# 이 Q라는 문자열이 K번 반복된다는 뜻이다. 
# 압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.

str=input()
stack=[]
num=0

for i,s in enumerate(str):
    # 문자 길이로 계산하기
    if s!="(" and s!=")":
        num+=1
    if s=="(":
        stack.append([num-1, int(str[i-1])]) # 앞에 문자 개수, 괄호 바로 앞에 있는 수
        num=0
    if s==")":
        if not stack:
            break
        else: 
            n=stack.pop()
            num=num*n[1]+n[0]
            
print(num)