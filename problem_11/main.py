

class Solution:
    def __init__(self):
        pass

    def max_4_product(self, matrix):
        """
        The input is a 20*20 matrix
        Note that the goal is to find the max product of four adjacent numbers in either of three directions
        """
        m = len(matrix)
        n = len(matrix[0])
        p = 4  # target number of diagonal elements
        max_prod = 0
        for i in range(m):
            for j in range(n):
                # Diagonal direction
                if i < m-p+1 and j < n-p+1:
                    prod = 1
                    for k in range(p):
                        prod *= matrix[i+k][j+k]
                    if prod > max_prod:
                        max_prod = prod
    
                # Horizontal direction
                if j < n-p+1:
                    prod = 1
                    for k in range(p):
                        prod *= matrix[i][j+k]
                    if prod > max_prod:
                        max_prod = prod

                # Vertical direction
                if i < m-p+1:
                    prod = 1
                    for k in range(p):
                        prod *= matrix[i+k][j]
                    if prod > max_prod:
                        max_prod = prod
        return max_prod

if __name__ == "__main__":
    # First process the data file
    matrix = []
    with open("grid.txt", "r") as f:
        for line in f:
            line_chars = line.replace('\n', '').replace('\r', '').split()
            matrix.append([int(c) for c in line_chars])
    
    print matrix
    s = Solution()
    print s.max_4_product(matrix)
