class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows - 1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr


print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("PAYPALISHIRING", 3))
