class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i , x in enumerate(nums):
            for j , y in enumerate(nums):
                if i == j:
                    continue
                elif (x + y == target):
                    return [i , j]