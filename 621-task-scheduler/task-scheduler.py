from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks).values()

        max_count = max(counts)
        max_tasks = list(counts).count(max_count)

        empty_slots = (max_count - 1) * (n + 1) + max_tasks

        return max(len(tasks), empty_slots)