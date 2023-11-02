class Solution(object):
    def check(self, nums):
        count=0
        rpoint=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                rpoint=i
                count+=1
        if count==0:
           return True
        elif count==1:
            nums=nums[rpoint:]+nums[:rpoint]
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
            return True
        else:
            return False

