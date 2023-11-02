def findMax(arr):
  max=0
  for i in range(len(arr)):
    if arr[i] > max:
      max= arr[i]
  return max


arr=[64,25,12,22,11]

max=findMax(arr)
print(max)