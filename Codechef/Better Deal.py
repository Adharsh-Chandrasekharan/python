for t in range(int(input())):
    a,b=map(int,input().split())
    a1=100-(a)
    b1=200-(b*2)
    if a1==b1:
        print("BOTH")
    elif a1<b1:
        print("FIRST")
    else:
        print("SECOND")
    