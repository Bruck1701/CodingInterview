class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1

        return len(haystack.split(needle)[0])


print(Solution().strStr(haystack="hello", needle="ll"))

print(Solution().strStr(haystack="aaaaa", needle="bba"))

# print(Solution().strStr(haystack="aaa", needle="aaaa"))


# print(Solution().strStr(haystack="mississippi", needle="issi"))


print(Solution().strStr(haystack="mississippi", needle="issipi"))
