def linearSearch(arr,num):
  for i in range(len(arr)):
    if arr[i]==num:
      return i
  return -1


arr = [1, 2, 3, 4, 5]
num = 5
val=linearSearch(arr,num)

print(val)