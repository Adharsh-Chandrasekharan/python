def getLongestSubarray(a:[int], k:int) -> int:
  n=len(a)
  left,right=0,0
  sum=a[0]
  maxLen=0
  while right<n:
    while left<=right and sum>k:
      sum-=a[left]
      left+=1
    if sum==k:
      maxLen = max(maxLen,right-left+1)
    right+=1
    if right<n :
      sum+=a[right]
  return maxLen

if __name__=="__main__":
  a=[2,3,5,1,9]
  k=10
  length=getLongestSubarray(a,k)
  print(length)