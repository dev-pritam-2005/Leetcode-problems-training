class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = set()
        # k= 0
        # for num in nums:
        #     if num not in  seen:
        #         seen.add(num)

        #         nums[k]=num
        #         k=k+1
        # return k

        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1] = nums[j]
                i=i+1
        return i+1