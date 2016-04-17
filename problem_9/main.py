

class Solution:
    def __init__(self):
        pass

    def ptriplet(self):
        # Scan b from 1 to 999 and find the answer (return product a*b*c)
        # See README.md for details
        for b in range(1, 1000):
            a = float(500000 - 1000*b)/ (1000 -b)
            if abs(a - int(a)) < 1e-6:
                return int(a) * b * int(1000-a-b)


if __name__ == "__main__":
    s = Solution()
    print s.ptriplet()
