

class Solution:
    def __init__(self):
        pass
    
    # A brute-force method: check each product in the window without skipping zeros. Simple but not as efficient
    def max_window_product(self, window_len, num_str): 
        # Specify a window length
        # input a num string rather than raw number integer since 1000-digit number is too big

        # Iterate through the number string; take care of the zero product situation
        prod_max = 0
        for i in range(len(num_str) - window_len):
            if '0' in num_str[i: i+window_len]:
                # product will be zero
                continue 
            else:
                prod = 1
                for j in range(window_len):
                    prod *= int(num_str[i+j])
                if prod > prod_max:
                    prod_max = prod
        return prod_max


if __name__ == "__main__":
    # Prepare number string and do some cleaning
    num_str = ""
    with open("num1000.txt", 'r') as f:
       for line in f:
           num_str += line.replace('\n', '').replace('\r', '')

    s = Solution()
    print s.max_window_product(13, num_str)
