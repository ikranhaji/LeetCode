class Solution(object):
       def compress(self, chars):
            count = 1
            right = 0
            idx = 0

            while right < len(chars):
                char = chars[right]
                while right + 1 < len(chars) and chars[right + 1] == char:
                    count += 1
                    right += 1
                chars[idx] = char 
                idx += 1
                if count > 1:
                    for digit in str(count):
                        chars[idx] = digit  
                        idx += 1
                count = 1
                right += 1

            return idx

        