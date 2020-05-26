

class Solution:

    d = {1: 1, 2: 11, 3: 21, 4: 1211, 5: 111221}

    def myCount(self, n):
        numberString = str(n)
        wordOutput = ""
        count = 1
        for i in range(1, len(numberString)):
            if numberString[i-1] == numberString[i]:
                count += 1
            else:

                wordOutput += str(count)+numberString[i-1]
                count = 1

        wordOutput += str(count)+numberString[i]

        return wordOutput

    def func(self, n):
        if n in self.d:
            return self.d[n]
        else:
            return int(self.myCount(self.func(n-1)))

    def countAndSay(self, n: int) -> str:
        return str(self.func(n))


# print(Solution().countAndSay(1))
# print(Solution().countAndSay(2))
# print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
print(Solution().countAndSay(6))
print(Solution().countAndSay(7))

# print(Solution().myCount(111221))
# print(Solution().myCount(1211))
