class Solution(object):
    def isPalindrome(self, x):
        lst=list(str(x))
        if lst==lst[::-1]:
            return True
        else:
            return False
        