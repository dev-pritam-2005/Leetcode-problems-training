class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [0]*len(nums)
        index=0

        for num in nums:
            if num!=0:
                temp[index]=num
                index += 1
        for i in range (len(nums)):
            nums[i]=temp[i]

        return nums



        # optimal
        # i=0
        # n=len(nums)
        # for j in range (n):
        #     if(nums[j]!=0):
        #         nums[j],nums[i]=nums[i],nums[j]
        #         i+=1
        