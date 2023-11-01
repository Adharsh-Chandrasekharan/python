from math import sqrt
for t in range(int(input())):
    a,b=map(int,input().split())
    sumab=a+b 
    c=0
    for i in range(2,round(sqrt(sumab))+1):
        if sumab%i==0:
            c+=1 
    if c==0:
        print("Alice")
    else:
        print("bob")