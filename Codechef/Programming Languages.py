# cook your dish here
for i in range(int(input())):
    #a,b,a1,b1,a2,b2=map(int,input().split())
    lst=list(map(int,input().split()))
    if (lst[0] in lst[2:4]) and (lst[1] in lst[2:4]):
        print(1)
    elif (lst[0] in lst[4::]) and (lst[1] in lst[4::]):
        print(2)
    else:
        print(0)