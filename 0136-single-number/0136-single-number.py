class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = 0

        # XOR all elements — duplicates cancel out
        for num in nums:
            xorr ^= num

        return xorr
        
        
        
        
        
        
        
        #better hash approach
        # maxi = max(nums)
        # hash_arr = [0] * (maxi + 1)

        # for num in nums:
        #     hash_arr[num] += 1

        # for i in range(maxi + 1):
        #     if hash_arr[i] == 1:
        #         return i

        # return -1









        # brute force : but time limit will exceed  : o(N2)
        # n= len(nums)
        # for i in range (n):
        #     ele = nums[i]
        #     count = 0
        #     for j in range (n):
        #         if nums[j]==ele:
        #             count+= 1
        #     if count == 1:
        #         return ele
        # return -1