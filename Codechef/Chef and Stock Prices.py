# cook your dish here
for i in range(int(input())):
    s,a,b,c=map(int,input().split())
    s=s+(s/100)*c
    if s>=a and s<=b:
        print("YES")
    else:
        print("NO")