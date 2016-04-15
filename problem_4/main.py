

class Solution:
    def __init__(self):
        pass
   
    def is_palindrome_1(self, num):
        """
        Find whether the input integer is a palindrome number
        """
        # First find out the length of integer
        n_digit = 0
        num2 = num
        while num2:
            num2 /= 10
            n_digit += 1

        for i in range(1, n_digit/2+1):
            if ( num / 10**(n_digit-1) ) != ( num % 10 ):
                return False
            # Now remove the tested digits in two end
            num %= 10**(n_digit -1)
            num /= 10
            n_digit -= 2
        return True

    def is_palindrome_2(self, num):
        """
        Another (more straightforward) way to test palindrome number
        """
        rev_num = 0
        temp = num
        while temp:
            rev_num *= 10
            rev_num += temp % 10
            temp /= 10
        return num == rev_num

    # A brute-force dumb solution with no mathematical twist
    # Simply iterate through all possible 3-digit cases
    def largest_palin_dumb(self):
        p_max = 0  # give it a small number to start with
        for n in range(100, 1000):
            for m in range(100, 1000):
                if self.is_palindrome_2(n*m) and (n*m) > p_max:
                    p_max = n*m 
        return p_max

    # Another quicker solution based on mathematical properties of this number is presented in the end of the "overview" pdf doc


if __name__ == "__main__":
    s = Solution()
    print s.largest_palin_dumb()
