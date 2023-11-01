def insertionSortRecursive(arr,i):
  key=arr[i]
  j=i-1
  while j>=0 and key<arr[j]:
    arr[j+1] = arr[j]
    j-=1
  arr[j+1] = key
  if i+1<len(arr):
    insertionSortRecursive(arr,i+1)
  return arr
arr=[64,25,12,22,11]
final= insertionSortRecursive(arr,0)
print(final)
