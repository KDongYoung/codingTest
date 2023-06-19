# 두 개의 영어 단어가 주어졌을 때, 
# 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오. 
# 문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.

# 문자열을 리스트로 변환
w1=list(input())
w2=list(input())

w11,w22=w1[:],w2[:]
        
for w in w1:
    if w in w22:
        w22.remove(w)
for w in w2:
    if w in w11:
        w11.remove(w)

print(len(w11)+len(w22))