# cook your dish here
for i in range(int(input())):
    n,s=map(int,input().split())
    if n>=s:
        print(s)
    else:
        print(2*n-s)
                