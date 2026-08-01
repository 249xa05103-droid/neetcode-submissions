class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1
        idx = 0

        while l1 <= r1:
            mid = (l1 + r1) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                idx = mid
                break

            if matrix[mid][-1] < target:
                l1 = mid + 1
            else:
                r1 = mid - 1

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[idx][mid] == target:
                return True
            if matrix[idx][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False