def sum_numbers(lst,sum):
  output=[]
  dif={}
  for i in lst:
    diff=sum-i
    if diff not in dif:
      dif[i]=diff
    if i in dif:
      print(i)


lst=[1,2,3,4,5,6,7,8,9]
sum=8
sum_numbers(lst,sum)