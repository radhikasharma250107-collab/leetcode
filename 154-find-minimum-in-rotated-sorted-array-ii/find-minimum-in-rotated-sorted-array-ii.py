class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = 0 
        end = len(nums)-1
        while st<end:
            mid = st + (end-st) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                st = mid+1
            else:
                end -= 1
        return nums[st]