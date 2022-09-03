# Runtime: 66ms (92.59%) Memory Usage: 15.2MB (23.96%) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(0,len(nums)):
            hm[nums[i]] = i
        for i in range(0,len(nums)):
            val = target - nums[i] 
            if val in hm and hm[val] != i:
                return [i,hm[val]]
