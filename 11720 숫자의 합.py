num=int(input())
a=int(input())
t=0
for i in range(num):
   t+=a%10
   a=a//10
print(t) 