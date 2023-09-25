#bitwise operator
def evenodd(n):
    if n&1==1:
        print("odd")
    else:
        print("even")

def mul(x,y):
    return x<<y

def div(x,y):
    return x>>y

t=int(input("Enter number of cases: "))
while t:
    x,y=map(int,input().split())
    print(mul(x,y))
    print(div(x,y))
    t=t-1
        
