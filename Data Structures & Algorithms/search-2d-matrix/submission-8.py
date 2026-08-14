class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            print("==============")
            left = 0
            right = len(row) - 1
            print("Left: ", left)
            print("Right: ", right)
            if target > row[right]:
                continue
            while left <= right:
                mid = int((left + right) // 2)
                print("Mid index: ", mid)
                print("Mid value: ", row[mid])
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
