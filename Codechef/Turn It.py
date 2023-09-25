# cook your dish here

for i in range(int(input())):
    u,v,a,s=map(int,input().split())
    sqv=u*u-2*a*s
    #print(sqv)
    if sqv<0:
        print("Yes")
    elif (sqv**0.5)<=v:
        print("Yes")
    else:
        print("No")
        
    