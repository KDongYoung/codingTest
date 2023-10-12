'''
한글 프로그램의 메뉴에는 총 N개의 옵션이 있다. 
각 옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명하여 놓았다. 
그리고 우리는 위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 하였다. 
단축키를 지정하는 법은 아래의 순서를 따른다.

1. 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 
   만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 
   단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
3. 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.
'''

import sys
input=sys.stdin.readline

num=int(input())
d=dict([])


for _ in range(num):
    ss=input().rstrip().split()
    flag=False

    t=[]
    
    for i in range(len(ss)):
        if not flag and ss[i][0].lower() not in d.keys():
            d[ss[i][0].lower()]=ss[i][1:]
            ss[i]=f'[{ss[i][0]}]{ss[i][1:]}'
            flag=True
    
    if not flag:
        for i in range(len(ss)):
            for j in range(len(ss[i])):
                if ss[i][j].lower() not in d.keys():
                    d[ss[i][j][0].lower()]=ss[i][j][1:]
                    ss[i]=ss[i][:j]+f'[{ss[i][j]}]'+ss[i][j+1:]
                    flag=True
                    break
            
            if flag:
                break
    
    print(" ".join(ss))