class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #now its time for optimal babe

        
        low, mid, high = 0, 0, len(nums) - 1

        
        while mid <= high:
            


            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            


            elif nums[mid] == 1:
                mid += 1
            


            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            
    
        
        
        
        
        #better not optimal 
        # cnt0 = cnt1=cnt2 = 0
        # n = len(nums)
        # for i in range (n):
        #     if nums[i]==0 :
        #         cnt0 +=1
        #     elif nums[i]==1:
        #         cnt1 += 1
        #     else:
        #         cnt2 +=1
        
        # for i in range(cnt0):
        #     nums[i] = 0
        # for i in range(cnt0,cnt0+cnt1):
        #     nums[i]=1   
        # for i in range(cnt0+cnt1 , n):
        #     nums[i]=2



        # brute force
        # brute force approach : although its not good 
        # def merge_sort(arr):
        #     if len(arr) <= 1:
        #         return arr

        #     mid = len(arr) // 2

        #     left = merge_sort(arr[:mid])
        #     right = merge_sort(arr[mid:])

        #     return merge(left, right)

        # def merge(left, right):
        #     result = []
        #     i = 0
        #     j = 0

        #     while i < len(left) and j < len(right):

        #         if left[i] <= right[j]:
        #             result.append(left[i])
        #             i += 1
        #         else:
        #             result.append(right[j])
        #             j += 1

        #     while i < len(left):
        #         result.append(left[i])
        #         i += 1

        #     while j < len(right):
        #         result.append(right[j])
        #         j += 1

        #     return result

        # sorted_arr = merge_sort(nums)

        # for i in range(len(nums)):
        #     nums[i] = sorted_arr[i]
        