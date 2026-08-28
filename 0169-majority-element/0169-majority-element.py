class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
       
       
       
       
       
       
        # brute : time limit exceed 
        # n = len(nums)

        # for i in range (n):
        #     cnt=0
        #     for j in range (n):
        #         if nums[i]==nums[j]:
        #             cnt +=1
        #     if cnt > n/2:
        #         return nums[i]
        # return -1



        # better : working good 
        # n=len(nums)

        # mp={

        # }

        # for num in nums:
        #     if num in mp:
        #         mp[num] += 1
        #     else:
        #         mp[num] = 1

        # for num, count in mp.items():
        #     if count > n // 2:
        #         return num

        # return -1

        # optimal 
        
        n = len(nums)
        
       
        cnt = 0
        
      
        el = 0
        
      
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        
       
        cnt1 = nums.count(el)
        
       
        if cnt1 > (n // 2):
            return el
        
        
        return -1


       


       
        # count = 0
        # candidate = 0
        
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #         count =1
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        
        # return candidate