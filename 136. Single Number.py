class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=[]
        for i in nums:
            if i in num:
                num.remove(i)
            else:
                num.append(i)
        return num.pop()