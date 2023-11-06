def majorityElement(nums):
  n=len(nums)
  for i in range(len(nums)):
    if nums.count(nums[i])> (n//2):
      return nums[i]

nums=[2,2,1,1,1,2,2 ] 
op=majorityElement(nums)
print(op)