class Solution:
    def reverse(self, x: int) -> int:
        intstr = str(x)
        value = 0

        if intstr[0] == "-":
            intstr = intstr[1:]
            invert = "-"+intstr[::-1]
            value = int(invert)

        else:
            value = int(intstr[::-1])

        mina = -2**31
        maxa = 2**31 - 1

        if value not in range(mina, maxa):
            return 0

        else:
            return value


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
