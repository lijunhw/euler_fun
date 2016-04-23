

class Solution:
    def __init__(self):
        self.letter_table = {0: "",
                             1: "one",
                             2: "two",
                             3: "three",
                             4: "four",
                             5: "five",
                             6: "six",
                             7: "seven",
                             8: "eight",
                             9: "nine",
                             10: "ten",
                             11: "eleven",
                             12: "twelve",
                             13: "thirteen",
                             14: "fourteen",
                             15: "fifteen",
                             16: "sixteen",
                             17: "seventeen",
                             18: "eighteen",
                             19: "nineteen",
                             20: "twenty",
                             30: "thirty",
                             40: "forty",
                             50: "fifty",
                             60: "sixty",
                             70: "seventy",
                             80: "eighty",
                             90: "ninety",
                             100: "hundred",
                             1000: "thousand"
                             }
     
        
    def letter_count(self, num):
        """
        Return the letter count of a given integer between 1 and 1000
        """
        letter_count_table = dict()
        # Convert the alphabets to numerics in the table
        for k in self.letter_table:
            letter_count_table[k] = len(self.letter_table[k])

        str_out = ""   # only for debugging purpose
        l_count = 0
        and_count = 0
        thousands = num/1000
        hundreds = (num % 1000) / 100
        rest = num % 100
        if rest <= 20: 
            rest_cnt = letter_count_table[rest]
            rest_str = self.letter_table[rest]
        else: 
            tens = rest / 10
            ones = rest % 10
            rest_cnt = letter_count_table[tens*10] + letter_count_table[ones]
            rest_str = self.letter_table[tens*10] + self.letter_table[ones]

        if thousands:
            str_out += self.letter_table[thousands] + self.letter_table[1000]
            l_count += letter_count_table[thousands] + letter_count_table[1000]
            and_count += 1

        if hundreds:
            str_out += self.letter_table[hundreds] + self.letter_table[100]
            l_count += letter_count_table[hundreds] + letter_count_table[100]
            and_count += 1
        
        if rest:
            str_out += rest_str
            l_count += rest_cnt
            and_count += 1
        
        and_count -= 1
        l_count += and_count*3  # don't forget "and"s
        # print str_out + and_count*"and"
        return l_count


    def lets_count(self):
        cnt = 0
        for i in range(1, 1001):
            cnt += self.letter_count(i)
        return cnt

if __name__ == "__main__":
    s = Solution()
    print s.lets_count()
    
