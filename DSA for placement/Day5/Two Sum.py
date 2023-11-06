def twosum(arr,target):
  op={}
  for i in range(len(arr)):
    diff=target-arr[i]
    if diff in op:
      return [i, op[diff]]
    else:
      op[arr[i]]=i
N = 5
arr = [2,6,5,8,11]
target = 14
op=twosum(arr,target)
print(op)