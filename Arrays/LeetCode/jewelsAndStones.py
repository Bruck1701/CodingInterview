'''
Jewels and Stones
How many jewels of J are in stones S?
'''


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        counter = 0
        for el in J:
            jewels[el] = True

        for el in S:
            if el in jewels:
                counter += 1
        return counter


print(Solution().numJewelsInStones(J="aA", S="aAAbbbb"))

print(Solution().numJewelsInStones(J="z", S="ZZ"))
