# cook your dish here
for i in range(int(input())):
    lst=list(map(int,input().split()))
    lst.sort()
    print(lst[-1]+lst[-2])
    