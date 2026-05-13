class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # frequency={}
        # n=len(nums)
        # for k in nums:0
        #     if k in frequency :
        #         frequency[k]=frequency[k]+1
        #     else:
        #         frequency[k]=1
        # for k in frequency:
        #     if frequency[k] > n//2 :
        #         return k 


       
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate