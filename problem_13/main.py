

class Solution:
    def __init__(self):
        pass

    def num_list_add(self, num_list1, num_list2):
        """
        A number list is a list of integers between 0~9. Format: 1234 --> [4,3,2,1]
        Return a number list
        """

        if len(num_list1) > len(num_list2):
            l1 = num_list2   # shorter list
            l2 = num_list1   # longer list
        else:
            l1 = num_list1
            l2 = num_list2
        
        num_list_res = [0 for _ in range(len(l2))]  # resulting number list
        carry = 0    # carry of each addition
        for i in range(len(l2)):
            if i < len(l1):
                res_i = l1[i] + l2[i] + carry
            else:
                res_i = l2[i] + carry
            num_list_res[i] = res_i % 10
            carry = res_i / 10
        if carry:
            num_list_res.append(1)
       
        return num_list_res

if __name__ == "__main__":
    s = Solution()
    # print s.num_list_add([8,4,3], [4, 5, 6])
    with open('numbers.txt', 'r') as f:
        res = [0]
        for line in f:
            # Convert a string line to a number list
            num_list = []
            for c in line.replace('\n', '').replace('\r', ''):
                num_list.insert(0, int(c))
            res = s.num_list_add(res, num_list)
    
    print res
    ten_digits = 0
    for i in range(10):
        ten_digits *= 10
        ten_digits += int(res[-1-i])
    print ten_digits




