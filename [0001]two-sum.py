class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in dict_nums:
                return [dict_nums[another], index]
            dict_nums[num] = index
        return None
