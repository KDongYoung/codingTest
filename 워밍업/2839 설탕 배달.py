sug=int(input())
bag=0

while sug >=0:
    if sug%5==0: # sug=0 되면 알아서 break
        bag+=sug//5
        print(bag)
        break
    else:
        sug-=3
        bag+=1  
    
else: 
    print(-1)