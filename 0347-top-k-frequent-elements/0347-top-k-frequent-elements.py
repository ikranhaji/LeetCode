class Solution(object):
    def topKFrequent(self, nums, k):
        dictionary = {}
        keys = []

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1

        sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            keys.append(sorted_items[i][0])

        return keys
    
            
            
    