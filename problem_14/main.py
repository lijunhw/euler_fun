
import math

class Solution:
    def __init__(self):
        pass

    # Brute-force
    def collatz_chain_len(self, num):
        chain_len = 0 
        while True:
            if num % 2:   # an odd number
                num = 3*num + 1
                chain_len += 1
            else:
                # the Collatz calculation can terminate early under certain condition below
                if abs(int(math.log(num, 2)) - math.log(num, 2)) < 1e-6:
                    chain_len += int(math.log(num,2)) + 1
                    return chain_len
                else:
                    num /= 2
                    chain_len += 1
    
    # Use a hash table to store previous Collatz numbers to speed up
    def collatz_chain_len_beta(self, num_init, cdict):
        # cdict = dict()
        num = num_init
        chain_len = 0 
        while True:
            if num in cdict:   # don't write like "if num in cdict.keys()": it is slow because an temperorary array will be created. 
                chain_len += cdict[num]
                cdict[num_init] = chain_len
                return chain_len
            
            chain_len += 1
            if num == 1:
                cdict[num_init] = chain_len
                return chain_len
            if num % 2:   # an odd number other than 1
                num = 3*num + 1
            else:
                num /= 2

    # Similar to the beta version, but doing it with dynamic programming
    def collatz_chain_len_gamma(self, num_init, cdict):
        # cdict holds each number and its number of Collatz chain stages
        if 1 not in cdict:
            cdict[1] = 1   # initial condition and base case
        
        def collatz_calc(num):  # a recursive implementation
            # The base case is already handled by the initial condition above
            if num not in cdict:
                if num % 2:  # odd number
                    num_next = 3*num + 1
                else:
                    num_next = num/2
                cdict[num] = collatz_calc(num_next) + 1

            return cdict[num]

        return collatz_calc(num_init)


if __name__ == "__main__":
    s = Solution()
    max_chain_len = 1
    max_chain_num = 1
    collatz_dict = dict()
    if 1:   
        for i in range(1, 10**6):
            # l = s.collatz_chain_len(i) # Solution 1: iterate through all possibility brute-force
            # l = s.collatz_chain_len_beta(i, collatz_dict)  # Solution 2: use a dictionary to cache previously calculated Collatz number. 
            l = s.collatz_chain_len_gamma(i, collatz_dict) 
            if l > max_chain_len:
                max_chain_len = l
                max_chain_num = i
        print max_chain_len, max_chain_num

    if 0:
        def sort_func(n):  # create a function wrapper as the "sort" function handler
            return s.collatz_chain_len_gamma(n, collatz_dict)
        print max(range(1, 10**6), key=sort_func)

