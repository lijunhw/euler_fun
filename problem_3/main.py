
import math

# Use Fermat's factorization method, which is a general method for integer factorization
# See algorithm at https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
class Solution:
    def __init__(self):
        pass

    def fermat_factorization(self, N):
        # Implement Fermat's factorization method
        # Goal: get a and b so that N == a**2 - b**2
        # Prerequisite: N is an odd integer
        a = int(math.ceil(math.sqrt(N)))
        b2 = a**2 - N   # b2 == b**2
        while abs(math.sqrt(b2) - int(math.sqrt(b2))) > 1e-6:  # meaning b is not a square number
            a += 1
            b2 = a**2 - N
        b = int(math.sqrt(b2))
        return int(a+b), int(a-b)
  
    def lpf_helper(self, num, container):
        # Use the container as the dirty trick to pass variable among recursive calls
        # Variable container is an array with 1 element, which is the max prime factor

        a, b = self.fermat_factorization(num)
        
        # Specify the base condition for the recursive call
        # That is, when input number is a prime number
        if b == 1:
            if a >= container[0]: 
                container[0]  = a
        else:
            self.lpf_helper(a, container)
            self.lpf_helper(b, container)
 
    def largest_prime_factor(self, num):
        if num == 2: 
            return 2
        
        container = [1]
        self.lpf_helper(num, container)
        return container[0]
        

if __name__ == "__main__":
    s = Solution()
    # print s.fermat_factorization(15)
    print s.largest_prime_factor(600851475143)

