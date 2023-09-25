from math import *
def fun(n):
  div=set()
  for i in range(1,int(sqrt(n))+1):
    if n%i==0:
      div.add(i)
      div.add(n//i)
  return div
t=int(input())
while t:
  n=int(input("Enter a number: "))
  div1=fun(n)
  print(*div1)
  t=t-1