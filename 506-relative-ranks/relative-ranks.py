class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
        ranks = {}

        for i, value in enumerate(sorted_scores):
            if i == 0:
                ranks[value] = "Gold Medal"
            elif i == 1:
                ranks[value] = "Silver Medal"
            elif i == 2:
                ranks[value] = "Bronze Medal"
            else:
                ranks[value] = str(i + 1)

        return [ranks[value] for value in score]