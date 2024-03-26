class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                        if count >= n:
                            return True
        return False