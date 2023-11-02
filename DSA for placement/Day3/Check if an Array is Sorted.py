def checkSorted(arr):
  for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
      return False
  return True



#arr=[64,25,12,22,11]
arr = [1, 2, 3, 4, 5]

if checkSorted(arr):
  print(True)
else:
  print(False)