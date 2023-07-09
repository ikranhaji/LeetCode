class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary= {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [word]
            else:
                dictionary[sorted_word] += [word]
        return [dictionary[i] for i in dictionary]
        