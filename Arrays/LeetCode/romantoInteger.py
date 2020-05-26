'''
O(N) solution
first is sums the face value of each symbol, then it looks for occurences of [IV,IX,XL,XC,CD,CM] if they are in the number,
you must take the lowest of the two numbers twice from the sum ( because it had ben added to it on the earlier loop ).

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        value = 0
        for el in s:
            value += d[el]

        idx = 0
        while idx < len(s)-1:
            if s[idx] == "I" and (s[idx+1] == "V" or s[idx+1] == "X"):
                value -= 2*d["I"]
            elif s[idx] == "X" and (s[idx+1] == "L" or s[idx+1] == "C"):
                value -= 2*d["X"]

            elif s[idx] == "C" and (s[idx+1] == "D" or s[idx+1] == "M"):
                value -= 2*d["C"]

            idx += 1

        return value


print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))

print(Solution().romanToInt("MM"))
print(Solution().romanToInt("CM"))
print(Solution().romanToInt("CMXLII"))
print(Solution().romanToInt("MMCMXLII"))
