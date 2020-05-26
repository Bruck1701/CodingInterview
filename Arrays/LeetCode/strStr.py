class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if len(needle) > len(haystack):
            return -1

        position = -1
        i = 0
        while i < len(haystack):
            letter = haystack[i]
            if letter == needle[0]:
                position = i
                j = i
                count = 0
                while count < len(needle) and j < len(haystack):
                    if haystack[j] == needle[count]:
                        j += 1
                        count += 1
                    else:
                        position = -1
                        break

                if count == len(needle):
                    return position

                if j == len(haystack) and count != len(needle):
                    return -1

            i += 1
        return position


# print(Solution().strStr(haystack="hello", needle="ll"))

# print(Solution().strStr(haystack="aaaaa", needle="bba"))

# print(Solution().strStr(haystack="aaa", needle="aaaa"))


# print(Solution().strStr(haystack="mississippi", needle="issi"))


print(Solution().strStr(haystack="mississippi", needle="issipi"))
