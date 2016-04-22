


class Solution:
    def __init__(self):
        pass

    # The idea is to convert the long integer to a list and define multiplication operation to avoid integer overflow
    def num_list_doubled(self, num_list):
        """
        Define 2x multiplication of the number list 
        Since Python passes list as an object (by reference), no need to return the resulting num_list
        """
        carry = 0
        for i in range(len(num_list)):
            prod = num_list[i] * 2 + carry
            num_list[i] = prod % 10
            carry = prod / 10

        if carry:
            num_list.append(carry)

    def twopower_digits_sum(self, power):
        nl = [1]
        for p in range(power):
            self.num_list_doubled(nl)
        s = 0
        for i in nl:
            s += i
        
        return s


if __name__ == "__main__":
    s = Solution()
    print s.twopower_digits_sum(1000)



