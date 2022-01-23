#第一次答案
#結果Time Limit Exceeded
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=int(2 * sum(set(nums)) - sum(nums)) 
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==a:
                    return nums[i],nums[j]
                
#第二次答案