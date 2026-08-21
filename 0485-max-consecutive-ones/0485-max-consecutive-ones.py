class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0
        mx_count=0
        for  i in range(len(nums)):
            if nums[i]==1:
                count +=1
            else:
                count =0
            mx_count= max(mx_count,count)
        return mx_count