'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    beginning = 1
    middle = 0
    end = 0

    def isBadVersion(self, number):
        # inserted here only to test the function
        if number >= 2:
            return True
        else:
            return False

    def recursiveSearch(self, beginning, middle, end):

        if beginning == end:
            return beginning

        if self.isBadVersion(middle) == False:
            return self.recursiveSearch(middle+1, int((middle+end)/2), end)
        else:
            return self.recursiveSearch(beginning, int((beginning+middle)/2), middle)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(self.recursiveSearch(1, int(n/2), n))


Solution().firstBadVersion(3)
