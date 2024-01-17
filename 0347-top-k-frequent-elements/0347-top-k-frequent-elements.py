class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        keys=[]
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            frequency[num] += 1
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse= True)
        for i in range(k):
            keys.append(sorted_frequency[i][0])
        return keys
            
        