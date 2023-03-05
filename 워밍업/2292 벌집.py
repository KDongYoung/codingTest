room = int(input())

# 1, 7, 19, 37 -> 6*i+1
j_num=1
cnt=1

while room > j_num:
    j_num += cnt*6
    cnt+=1

print(cnt)