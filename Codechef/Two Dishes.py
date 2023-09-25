# cook your dish here
for i in range(int(input())):
    n,a,b,c=map(int,input().split())
    if b>=n and a+c>=n:
        print("YES")
    else:
        print("NO")