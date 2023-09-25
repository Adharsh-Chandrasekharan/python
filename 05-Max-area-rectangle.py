def rectangle(n_sticks,lengths):
  arr=[]
  for stk in lengths:
    if lengths.count(stk)>=2 and stk not in arr:
      arr.append(stk)
  max_area=0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]*arr[j]>max_area:
        max_area=arr[i]*arr[j]
  return max_area
    

print(rectangle(8,[4,2,3,2,3,4,5,1]))

