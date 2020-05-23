'''
Bad Version Problem

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
