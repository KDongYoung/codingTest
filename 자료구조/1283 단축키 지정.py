'''
한글 프로그램의 메뉴에는 총 N개의 옵션이 있다. 
각 옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명하여 놓았다. 
그리고 우리는 위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 하였다. 
단축키를 지정하는 법은 아래의 순서를 따른다.

1. 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 
지정되었는지 살펴본다. 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 
   보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
3. 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.
'''

n=int(input())
# words=[]
d=[]

for _ in range(n):
    word=input().split()

    flag=False
    for i in range(len(word)):
        if flag:
            break
        if word[i][0].upper() not in d and word[i][0].lower() not in d:
            d.append(word[i][0])
            word[i]="["+word[i][0]+"]"+word[i][1:]
            # words.append(" ".join(word))
            flag=True
            break
    if flag:
        print(" ".join(word))
        continue            
    
    flag=False
    for i in range(len(word)):
        for j in range(len(word[i])):
            if word[i][j].upper() not in d and word[i][j].lower() not in d:
                d.append(word[i][j])
                word[i]=word[i][:j]+"["+word[i][j]+"]"+word[i][j+1:]
                # words.append(" ".join(word))  
                flag=True        
                break
            
        if flag:
            break

    print(" ".join(word))