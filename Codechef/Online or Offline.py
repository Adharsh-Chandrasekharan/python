for t in range(int(input())):
    n,m = map(int,input().split())
    n_new=(n-n*(10/100))
    if n_new<m:
        print("ONLINE")
    elif n_new==m:
        print("EITHER")
    else:
        print("DINING")