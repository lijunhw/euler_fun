"""
Project Euler Problem 1
"""

# The obvious solution 
# Time complexity: O(N)
def multiple_35(n_max): 
    s = 0
    for i in range(n_max):  # doesn't include n_max itself
        if ((i % 3) == 0) or ((i % 5) ==0):
            s += i
    return s


# A more "mathematical" solution
# Numbers divisible by x within [1, n) are arithmetic series. 
# The sum of all numbers in this series is p*(p+1)/2 with p == n/x
# Time complexity: O(1)
def multiple_35b(n_max):
    def sum_divisible_helper(x):
        p = n_max / x
        return x* p*(p+1)/2

    # Result should remove the double counted ones that are divisible by 15
    return sum_divisible_helper(3) + sum_divisible_helper(5) - sum_divisible_helper(15)


if __name__ == "__main__":
    print "Dumb solution:"
    print multiple_35(1000)

    print "Solution with more math flavor:"
    print multiple_35b(1000)


