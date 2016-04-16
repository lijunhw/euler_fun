
import math

class Solution:
    def __init__(self):
        pass

    def prime_num_gen(self, n_th):
        """
        n_th: n-th prime number to be generated
        Return: n-th prime number
        
        Probably still a very dumb way to generate prime numbers
        Idea: 
        1. A composite number is divisible by at least one prime number
        2. A prime number larger than 2 is an odd number
        
        Method: 
        Check each number starting from 3 with step of 2 incrementally, and scan it w.r.t. previous prime numbers between 3 and sqrt(num)
        """
        if n_th == 1:
            return 2
        prime_num_list = [2]
        num = 3  # testing number, starting from 3
        while len(prime_num_list) < n_th:
            num_ub = math.floor(math.sqrt(num))
            for n in prime_num_list:
                if n <= num_ub: # No need to check numbers larger than sqrt(num)
                    if num % n == 0:  
                        # not a prime number, no need to iterate further
                        break
                    else:
                        continue
                else:
                    # Now it is a prime number
                    prime_num_list.append(num)
                    break
            num += 2

        return prime_num_list[-1]


if __name__ == "__main__":
    s = Solution()
    print s.prime_num_gen(10001)


