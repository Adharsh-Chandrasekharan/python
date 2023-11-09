def findLeader(arr):
  arr_new=[]
  max=0
  for i in range(len(arr)-1,0,-1):
    if arr[i]>max:
      max=arr[i]
      arr_new.insert(0,arr[i])


  return arr_new

arr = [10, 22, 12, 3, 0, 6]
newArr=findLeader(arr)

for i in newArr:
  print(i,end=" ")