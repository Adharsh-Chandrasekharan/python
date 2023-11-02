def secondSmall(arr,n):
  if (n<2):
    return -1
  small=float('inf')
  second_Small=float('inf')
  for i in range(n):
    if (arr[i]< small):
      second_Small = small
      small = arr[i]
    elif (arr[i]< second_Small and arr[i]!=small):
      second_Small=arr[i]
  return second_Small

def secondLarge(arr,n):
  if (n<2):
    return -1
  large=float('-inf')
  second_Large=float('-inf')
  for i in range(n):
    if (arr[i] > large):
      second_Large = large
      large = arr[i]
    elif (arr[i] > second_Large and arr[i]!=large):
      second_Large=arr[i]
  return second_Large

arr=[64,25,12,22,11]
secondL= secondLarge(arr,len(arr))
seconds= secondSmall(arr,len(arr))

print(seconds)
print(secondL)