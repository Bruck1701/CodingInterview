'''
is palindrome no conversion into string
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        pos_num = []
        while x != 0:
            pos_num.append(x % 10)
            x = x // 10

        while len(pos_num) > 1:
            first = pos_num.pop(0)
            last = pos_num.pop()
            if first != last:
                return False

        return True


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(1221))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12351))
