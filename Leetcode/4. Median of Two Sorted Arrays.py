class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        li=nums1+nums2
        li.sort()
        length=len(li)
        if length%2==0:
            mid1=li[((length//2)-1)]
            mid2=li[(length//2)]
            mid=mid1+mid2
            sum=float(mid)/2
            return sum
        else:
            return li[length/2]

        