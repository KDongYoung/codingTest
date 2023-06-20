# C 표준 라이브러리는 문자열을 다루는 데에 매우 유용한 함수들을 제공하고 있다 
# 그들 중에는 strcpy, strcmp, strtol, strtok, strlen, strcat 가 있다.

# + strfry 함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어낸다.

# 두 개의 문자열에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지 판단하라.


n = int(input())
ans=[]
for _ in range(n):
    a,b = input().split()
    a,b = list(a), list(b)
    a.sort()
    b.sort()
    
    if len(a) != len(b):
        ans.append("Impossible")
    else:
        if sum([a[i]==b[i] for i in range(len(a))])!=len(a):
            ans.append("Impossible")
        else:
            ans.append("Possible")
    
for an in ans:
    print(an)
