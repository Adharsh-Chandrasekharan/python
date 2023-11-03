# cook your dish here
for t in range(int(input())):
    n=int(input())
    sum1=0
    i=1
    count=0
    while(sum1<=n):
        sum1=sum1+i
        i+=1
        count+=1
    print(count-1) 
    