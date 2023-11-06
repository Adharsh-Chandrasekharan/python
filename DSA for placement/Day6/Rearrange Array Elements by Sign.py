def rearrange(arr):
  n=len(arr)
  ans=[0]*n
  pInd,nInd=0,1
  for i in range(n):
    if arr[i]<0:
      ans[nInd]=arr[i]
      nInd+=2
    else:
      ans[pInd]=arr[i]
      pInd+=2
  return ans




arr=[1,2,-3,-1,-2,3]
ans=rearrange(arr)
print(ans)