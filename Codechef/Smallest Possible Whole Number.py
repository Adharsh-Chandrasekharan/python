# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    if n<k:
        print(n)
    elif k==0:
        print(n)
    else:
        print(n%k)