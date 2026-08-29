class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        j = 0
        maxi = 1
        while j < len(arr) - 1:
            if arr[j] == arr[j + 1]:
                i = j + 1
            elif j == i or (
                (arr[j - 1] < arr[j] and arr[j] > arr[j + 1]) or
                (arr[j - 1] > arr[j] and arr[j] < arr[j + 1])
            ):
                maxi = max(maxi, j - i + 2)
            else:
                i = j
            j += 1
        return maxi