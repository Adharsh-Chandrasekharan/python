def BinarySearch(arr,low,high, target):
  if low> high:
    return -1
  mid =(low+high)//2
  if arr[mid]== target:
    return mid
  elif target> arr[mid]:
    return BinarySearch(arr, mid+1,high,target)
  return BinarySearch(arr,0,mid-1,target)




arr=[3, 4, 6, 7, 9, 12, 16, 17]
target = 6

findIndex= BinarySearch(arr,0,len(arr),target)
if findIndex==-1:
  print("Element not found")
else:
  print("Element found at index",findIndex)