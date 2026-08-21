class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            if i in counts:
                return True
            counts[i] = 1   
        return False
        
# simplest is put in set and check if there is difference in counts
        