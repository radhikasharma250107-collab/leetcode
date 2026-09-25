from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        queue = deque()  # stores indexes

        for i in range(len(nums)):
            # Remove indexes outside the current window
            if queue and queue[0] < i - k + 1:
                queue.popleft()

            # Remove smaller values from the back
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            # Start adding results once the first window is complete
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result