class Solution:
    def solve(self , idx : int , prev : int ,  nums : List[int] , local_maxi : int ,  maxi : int) -> int:
        if idx >= len(nums):
            maxi = max(local_maxi , maxi)
            return maxi
        
        if nums[idx] == nums[prev]:
            return self.solve(idx + 1 , prev + 1 , nums , local_maxi , max(maxi , local_maxi))
        elif nums[idx] == nums[prev] + 1:
            local_maxi += 1
            return self.solve(idx + 1 , prev + 1 , nums , local_maxi , max(maxi , local_maxi))
        else:
            return self.solve(idx + 1 , prev + 1 , nums , 1  , maxi)
    
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        if len(nums) == 0:
            return 0
        # return self.solve(1 , 0 , nums , 1 , 1)

        maxi = 1
        local_maxi = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                local_maxi += 1
            else:
                local_maxi = 1
        
            maxi = max(local_maxi , maxi)
        return maxi