class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket = {}

        for char in s:
            if char not in bucket:
                bucket[char] = 1
            else:
                bucket[char] += 1
        
        for char in t:
            if char not in bucket:
                return False
            else:
                bucket[char] -= 1
        
        for i in bucket:
            if bucket[i]!= 0:
                return False

        return True
