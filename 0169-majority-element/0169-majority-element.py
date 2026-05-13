class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency={}
        n=len(nums)
        for k in nums:
            if k in frequency :
                frequency[k]=frequency[k]+1
            else:
                frequency[k]=1
        for k in frequency:
            if frequency[k] > n//2 :
                return k 
            