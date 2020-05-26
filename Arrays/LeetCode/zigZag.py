'''
ZigZag Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        intColumns = numRows-2

        s = list(s)
        bigRow = True
        bigRowList = []
        smallRowList = []
        while s != []:
            if bigRow:
                value = s[0:numRows]
                if len(value) < numRows:
                    value.extend((numRows-len(value))*[""])

                bigRowList.append(value)
                s = s[numRows:]

                bigRow = False
            else:
                bigRow = True
                value = [""]
                value.extend(s[0:intColumns])
                value.extend((numRows-len(value))*[""])

                smallRowList.append(value[::-1])
                s = s[intColumns:]
                bigRow = True

        for index in range(len(smallRowList)):
            srow = smallRowList[index]
            bigRowList[index] = ["".join(x)
                                 for x in zip(bigRowList[index], srow)]

        #print(bigRowList, smallRowList)
        i = 1
        while i < len(bigRowList):
            bigRowList[0] = ["".join(x)
                             for x in zip(bigRowList[0], bigRowList[i])]
            i += 1
        # print(bigRowList)

        return "".join(bigRowList[0])
        #print(bigRowList, smallRowList)


print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("PAYPALISHIRING", 3))


print(Solution().convert("ABCDE", 4))
