class Solution(object):
    def twoSum(self, nums, target):
        output={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in output:
                return [output[diff],i]
            else:
                output[nums[i]]=i
        