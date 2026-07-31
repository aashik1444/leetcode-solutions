class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # formula for column index, i = found value // no.of columns
        # formula for row index, j = found value % no.of columns
        m = len(matrix) #no.of rows
        n = len(matrix[0]) #no.of columns
        t = m * n #total no.of elements
        l, r = 0, t - 1

        while l <= r:
            m = (l + r) // 2
            i = m // n
            j = m % n

            middle_val = matrix[i][j]

            if target == middle_val:
                return True
            elif target < middle_val:
                r = m - 1
            else:
                l = m + 1

        return False