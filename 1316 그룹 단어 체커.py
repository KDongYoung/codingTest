num=int(input())
k=0

for i in range(num):
    strin=input()
    
    s_list=[i for i in strin]
    uniq=list(set(s_list))
    cnt=dict()
    k+=1
    
    for j, w in enumerate(s_list):
        if w not in cnt.keys():
            cnt[w]=[j]
        else:                 
            if len(cnt[w])==1:
                if cnt[w][0]==j-1:
                    cnt[w].append(j)
                else:
                    k-=1
                    break
            else:
                if cnt[w][-1]==j-1:
                    cnt[w].append(j)
                else:
                    k-=1
                    break
                       
    
print(k)
