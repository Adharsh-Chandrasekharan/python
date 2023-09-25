# cook your dish here
for i in range(int(input())):
    d,l,r=map(int,input().split())
    if d<l:
        print("Too Early")
    elif d>r:
        print("Too Late")
    elif d>=l and d<=r:
        print("Take second dose now")