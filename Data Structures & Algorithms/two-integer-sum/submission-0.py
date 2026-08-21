class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_checker = {}
        #store index for future lookup one pass sol
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_checker:
                return [complement_checker[complement], i]
            complement_checker[num] = i