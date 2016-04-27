
# Use num list trick to do large number multiplication
# Num list format example: 1234 --> [4, 3, 2, 1]


# This solution is kinda reinventing the wheel in handling the large factorial number. 
# It is not very efficient because one can simply use Python's built-in factorial function, which is actually fast and can handle large numbers. 
# This solution just shows the thinking process. 
class Solution:
    def __init__(self):
        pass
        
    def num_list_add(self, num_list_1, num_list_2):
        """
        Implement the addition of two num lists
        Return another num list
        The implementation is not really efficient, but works
        """
 
        if len(num_list_1) > len(num_list_2):
            nl_s = num_list_2
            nl_l = num_list_1
        else:
            nl_s = num_list_1
            nl_l = num_list_2

        num_list_res = [0 for _ in range(len(nl_l))]
        carry = 0
        for i in range(len(nl_l)):
            if i < len(nl_s):
                s = nl_s[i] + nl_l[i] + carry
            else:
                s = nl_l[i] + carry
            carry = s/10
            num_list_res[i] = s%10
        if carry:  # take care of the last carry
            num_list_res.append(carry)

        return num_list_res
            

    def num_list_multiply(self, num_list_1, num_list_2):
        """
        Define multiplication of 2 number lists, and return another num list
        Mimic the normal multiplication process
        """
        carry = 0
        num_list_res = [0]
        for i in range(len(num_list_1)):
            carry = 0
            num_list_iter = [0 for _ in range(len(num_list_2))]
            for j in range(len(num_list_2)):
                prod = num_list_2[j] * num_list_1[i] + carry
                carry = prod / 10
                num_list_iter[j] = prod % 10
            if carry:
                num_list_iter.append(carry)

            for k in range(i):  # insert zeros after the least significant digit to mimic x10 multiplication
                num_list_iter.insert(0, 0)
            num_list_res = self.num_list_add(num_list_res, num_list_iter)

        return num_list_res


    def num_list_convert(self, num):
        """
        Convert a number to a num list
        """
        num_list = [num % 10]
        while num/10:
            num /= 10
            num_list.append(num%10)
        return num_list


    # main function here
    def digit_sum_factorial(self, num):
        """
        Sum of the digits of a factorial number
        """

        # Count the number of factors of 2 and 5 since 2*5 won't contribute to the digit sum in the end
        cnt_2 = 0
        cnt_5 = 0
        
        # This array host the remaining factors (don't have to be prime numbers)
        remaining = []
        
        for n in range(2, num+1):
            while n%2 == 0:
                n /= 2
                cnt_2 += 1
            while n%5 == 0:
                n /= 5 
                cnt_5 += 1
            if n != 1:
                remaining.append(n)
        
        remaining_prod = [1]
        if cnt_2 > cnt_5:
            remaining.append(2**(cnt_2-cnt_5))
        elif cnt_2 < cnt_5:
            remaining.append(5**(cnt_5-cnt_2))

        # Multiply all elements in the "remaining"
        for n in remaining:
            nl = self.num_list_convert(n)
            remaining_prod = self.num_list_multiply(nl, remaining_prod)

        # Finally do the digit sum
        s = 0
        for n in remaining_prod: 
            s += n
        return s


if __name__ == "__main__":
    s = Solution()
    # print s.num_list_multiply([1,2], [3, 4, 5])
    print s.digit_sum_factorial(100)


