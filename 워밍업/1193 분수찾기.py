# 1+2+3+4+5 ....  1+i

num=int(input())
cnt=1

while cnt<num:
    num-=cnt
    cnt+=1
# num행 cnt열  위치

if cnt%2==0:
    a=num
    b=cnt-num+1
else:
    a=cnt-num+1
    b=num

print(str(a)+"/"+str(b))