class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            st_word = ''.join(sorted(word))
            if st_word not in res:
                res[st_word] = []
            res[st_word].append(word)
        return res.values()