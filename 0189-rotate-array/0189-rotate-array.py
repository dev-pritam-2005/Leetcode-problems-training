class Solution:
    def reverse(self, nums, start, end):
        # Swap elements from start to end
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n = len(nums)

        # Edge case: no rotation needed
        if n == 0 or k == 0:
            return nums

        # Normalize k if it's larger than n
        k = k % n

          # If direction is right
            # if direction == "right":
            # Step 1: reverse the entire array
        self.reverse(nums, 0, n - 1)

            # Step 2: reverse first k elements
        self.reverse(nums, 0, k - 1)

            # Step 3: reverse remaining n-k elements
        self.reverse(nums, k, n - 1)






        # n= len(nums)
        # if n == 0:
        #     return
        
        # k%=n

        # temp=nums[-k:]

        # for i in range(n-k-1,-1,-1):
        #     nums[i+k] = nums[i]
        # for i in range(k):
        #     nums[i]=temp[i]