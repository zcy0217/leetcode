#第一次答案
#結果Time Limit Exceeded
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=nums.copy()
        for i in range(len(nums)): #因為每個數字不是出現一次就是三次所以三個迴圈ijk
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if (i != j != k) and (nums[i]==nums[j]==nums[k]): #索引值不相同and三個元素數字相同
                        num[i]=num[j]=num[k]=0 #將複製的串列的元素更改成0
                    else: #索引值相同
                        continue
        for num in num:
            if num!=0: #輸出num裡面不等於0的數字
                return num
#%%
#第二次答案
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums)) / 2) 
'''
取set後總和*3減所有元素總和除2
ex:[a, a, a, b, b, b, c, c, c, d] 
( 3*(a+b+c+d) – (a + a + a + b + b + b + c + c + c + d) ) / 2
出來的值會是float所以要加int括在外面
'''