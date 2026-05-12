class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowerBound(arr, target):
            low = 0
            high = len(arr) - 1
            lb = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    lb = mid
                    high = mid - 1

                elif arr[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            return lb

        def upperBound(arr, target):
            low = 0
            high = len(arr) - 1
            ub = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    ub = mid
                    low = mid + 1

                elif arr[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            return ub

        return [lowerBound(nums, target),
                upperBound(nums, target)]