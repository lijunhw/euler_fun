
import math
import itertools as it


class Solution:
    def __init__(self):
        pass

    # Borrow Fermat's factorization routine from Problem 3
    def fermat_factorization(self, N):
        # Implement Fermat's factorization method
        # Goal: get a and b so that N == a**2 - b**2
        # Prerequisite: N is **an odd integer**
        a = int(math.ceil(math.sqrt(N)))
        b2 = a**2 - N   # b2 == b**2
        while abs(math.sqrt(b2) - int(math.sqrt(b2))) > 1e-6:  # meaning b is not a square number
            a += 1
            b2 = a**2 - N
        b = int(math.sqrt(b2))
        return int(a+b), int(a-b)
    
    def factorize_odd_number(self, num, dict_factor):
        """
        The input num must be an odd number so that it can be processed by Fermat factorization
        dict_factor: a dictionary object passed among recursive calls
        dict_factor is a hash table with prime factor as the key, and power as the value
        For example, num==15 will result in dict_factor of {3:1, 5:1} since 15 = 3*5
        
        """
        n1, n2 = self.fermat_factorization(num)
        if n2 == 1:   # base case: n1 is a prime number
            if dict_factor.has_key(n1):
                dict_factor[n1] += 1
            else:
                dict_factor[n1] = 1
        else:   # n1 is not a prime number yet
            self.factorize_odd_number(n1, dict_factor)
            self.factorize_odd_number(n2, dict_factor)
        
    # My original dumb way to count number of divisors
    def triangle_divisor_num(self, k):
        """
        Return the number of divisors of k-th triangle number
        """
        if k == 1:
            return 1

        # First calculate triangle number
        num = k * (k+1)/2

        dict_factor = dict()
        # Reduce the number to an odd number so that it can be processed by Fermat factorization
        dict_factor[2] = 0
        while num % 2 ==0:
            num /= 2
            dict_factor[2] += 1
            
        self.factorize_odd_number(num, dict_factor)
        power_list = []
        for k in dict_factor.values():
            power_list.append(k)
        
        dnum = 0  # number of divisors
        for i in range(1, len(power_list)+1):
            comb = list(it.combinations(power_list, i))  # return a list of tuples
            # print comb
            for c in comb:  # c is a tuple
                prod = 1
                for cc in c:
                    prod *= cc
                dnum += prod
        dnum += 1   # in the end don't forget 1 is also a divisor
        return dnum

    # Easier way to count
    def triangle_divisor_num_simple(self, k):
        """
        Return the number of divisors of k-th triangle number
        """
        if k == 1:
            return 1

        # First calculate triangle number
        num = k * (k+1)/2

        dict_factor = dict()
        # Reduce the number to an odd number so that it can be processed by Fermat factorization
        dict_factor[2] = 0
        while num % 2 ==0:
            num /= 2
            dict_factor[2] += 1
            
        self.factorize_odd_number(num, dict_factor)
        
#        # k-th triangle number == k*(k+1)/2
#        # Break up the triangle number for faster factorization
#        # num = p1*p2, with p1 guranteed to be odd
#        if k % 2: 
#            p1 = k         # guranteed to be odd
#            p2 = (k+1)/2   # may be odd or even
#        else:
#            p1 = k+1
#            p2 = k/2
#
#        dict_factor = dict()
#        # Reduce p2 to an odd number so that it can be processed by Fermat factorization
#        dict_factor[2] = 0
#        while p2 % 2 ==0:
#            p2 /= 2
#            dict_factor[2] += 1
#            
#        self.factorize_odd_number(p1, dict_factor)
#        self.factorize_odd_number(p2, dict_factor)

        dnum = 1
        for v in dict_factor.values():
            dnum *= v+1
        return dnum
 

if __name__ == "__main__": 
    s = Solution()
    k = 1
    dn = 1
    while dn < 500:
        k += 1 
        dn = s.triangle_divisor_num_simple(k)
        
    print k*(k+1)/2    # calculate the final triangle number
