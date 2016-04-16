
class Solution:
    def __init__(self):
        pass
    
    # Solution 1: simply adding up the cross terms
    def sum_square_diff(self, N):
        s = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i!=j:
                    s += i*j
        return s
    
    # Solution 2: use the mathematical formulas
    def sum_square_diff_math(self,N):
        square_sum = ( N*(N+1)/2 )**2
        sum_square = (2*N+1) * (N+1) * N /6
        return square_sum - sum_square


if __name__ == "__main__":
    s = Solution()
    print s.sum_square_diff_math(100)

