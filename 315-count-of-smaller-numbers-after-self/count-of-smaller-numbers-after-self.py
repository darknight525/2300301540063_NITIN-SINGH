class Solution:
    def countSmaller(self, nums):

        res = [0] * len(nums)

        arr = list(enumerate(nums))

        def mergeSort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            merged = []

            i = j = 0

            while i < len(left) and j < len(right):

                if left[i][1] <= right[j][1]:

                    res[left[i][0]] += j
                    merged.append(left[i])
                    i += 1

                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                res[left[i][0]] += j
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        mergeSort(arr)

        return res
        