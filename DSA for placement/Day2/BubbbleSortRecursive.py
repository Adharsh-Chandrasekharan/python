def BubbleSortRecursive(arr):
  for i in range(len(arr)):
    try:
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        BubbleSortRecursive(arr)
    except IndexError:
      pass
  return arr

arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(arr)
final=BubbleSortRecursive(arr)
print("\nSorted array is ")
print(final)