a=int(input())
b=input()

for i in range(len(b)):
    print(a*int(b[len(b)-i-1]))
print(a*int(b))
