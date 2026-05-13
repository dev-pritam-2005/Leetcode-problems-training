class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSortedArray(arr1, arr2):
            i, j = 0, 0
            result = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
            result.extend(arr1[i:])
            result.extend(arr2[j:])
            return result

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return mergeSortedArray(left, right)

        return mergeSort(nums)