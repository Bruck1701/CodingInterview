from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        middle = int(len(s)/2)
        last = len(s)-1
        for i in range(middle):
            s[i], s[last-i] = s[last-i], s[i]
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))

print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))
