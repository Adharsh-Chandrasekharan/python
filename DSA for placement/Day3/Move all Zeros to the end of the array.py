def movezeros(arr):
  final=[]
  for i in range(len(arr)):
    if arr[i]!=0:
      final.append(arr[i])
  remaining=len(arr)-len(final)
  for i in range(remaining):
    final.append(0)
  print(final)

arr=list(map(int,input("Enter array").split(',')))
movezeros(arr)