"""
Defang IP address
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        hashmap = {}
        for el in address:
            if el not in hashmap:
                hashmap[el] = el

        hashmap["."] = "[.]"

        output = ""
        for el in address:
            output += hashmap[el]

        return output


print(Solution().defangIPaddr("1.1.1.1"))
