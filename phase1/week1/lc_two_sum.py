from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i, val1 in enumerate(nums):
        #     num1 = val1
        #     for j,val2 in enumerate(nums[i+1:]):
        #         num2 = val2
        #         if num1 + num2 == target:
        #             return [i,j + (i + 1)]

        dict1 = {}
        for index, value in enumerate(nums):
            num2 = 0
            num2 = target - value
            if num2 in dict1:
                return [dict1[num2], index]
            dict1[value] = index
