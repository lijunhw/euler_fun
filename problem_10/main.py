
import math

class Solution:
    def __init__(self):
        pass

    # This solution borrows idea from Problem 7 ("10001st prime")
    # A natural brute-force approach
    def prime_num_sum(self, num_max):
        """
        num_max: maximum prime number to be generated
        Return: sum of all prime numbers up to num_max
        
        Probably still a very dumb way to generate prime numbers
        Idea: 
        1. A composite number is divisible by at least one prime number
        2. A prime number larger than 2 is an odd number
        
        Method: 
        Check each number starting from 3 with step of 2 incrementally, and scan it w.r.t. previous prime numbers between 3 and sqrt(num)
        """
        if num_max == 2:
            return 2
        prime_num_list = [2]
        num = 3  # testing number, starting from 3
        while num <= num_max:
            n_ub = math.floor(math.sqrt(num))  # set the scanning upper bound
            for n in prime_num_list:
                if n <= n_ub: # No need to check numbers larger than sqrt(num)
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
        p_sum = 0
        for p in prime_num_list:
            p_sum += p
        return p_sum


    def prime_num_sum_sieve(self, num_max):
        """
        Use [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to find prime numbers below a limit
        """

        if num_max == 2:
            return 2
        # Start with a bag of all odd numbers below num_max
        bag = set()   # use set(), an unordered list
        bag.add(2)
        for i in range(1, num_max/2):
            bag.add(2*i +1)
        if num_max % 2:  # num_max is an odd number
            bag.add(num_max)

        num_next = 3
        # Note that it is enough to set the scanning upper bound to sqrt(num_max) rather than num_max 
        # The reason is any composite number larger than sqrt(num_max) have already been eliminated by previous iterations
        while num_next <= math.floor(math.sqrt(num_max)):  
            if num_next in bag:
                # If still in the bag, then it is the next prime number
                # Now remove the multiples of num_next from the bag
                # Again, only check the odd number to save time
                i = 3
                while i*num_next <= num_max: 
                    if i*num_next in bag:
                        bag.remove(i*num_next)
                    i += 2
            num_next += 2

        # Now pop out all elements in the bag and sum them over
        p_sum = 0
        for _ in range(len(bag)):
            nn = bag.pop()
            p_sum += nn
            #print nn

        return p_sum



if __name__ == "__main__":
    s = Solution()
    #print s.prime_num_sum(2000000)
    # print s.prime_num_sum(2000000)
    print s.prime_num_sum_sieve(2000000)
