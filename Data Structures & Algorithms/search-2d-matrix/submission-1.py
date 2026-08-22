class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1

        while u <= d:
            m = u + (d - u) // 2

            if target < matrix[m][0]:
                d = m - 1

            elif target > matrix[m][0]:
                if m + 1 == len(matrix) or (m + 1 < len(matrix) and target < matrix[m + 1][0]):

                    l, r = 0, len(matrix[m]) - 1
                    
                    while l <= r:
                        m2 = l + (r - l) // 2
                        if target < matrix[m][m2]:
                            r = m2 - 1
                        elif target > matrix[m][m2]:
                            l = m2 + 1
                        else:
                            return True 
                    return False

                else:
                    u = m + 1

            else:
                return True

        return False