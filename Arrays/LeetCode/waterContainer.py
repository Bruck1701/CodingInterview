# BRUTE FORCE APPROACH O(N^2)

# from itertools import combinations


# class Solution:
#     def maxArea(self, height):

#         if len(height) == 2:
#             return min(height[0], height[1])

#         subset = combinations(height, 2)

#         floor = 1
#         maxFloor = len(height)-1
#         maxArea = 0

#         for el in subset:
#             area = floor*min(el[0], el[1])
#             if area > maxArea:
#                 maxArea = area

#             if floor < maxFloor:
#                 floor += 1
#             else:
#                 floor = 1
#                 maxFloor -= 1

#         return(maxArea)

#print([x for x in subset])


# two pointers approach:


class Solution:
    def maxArea(self, height):
        init = 0
        end = len(height)-1
        maxArea = 0

        while init != end:
            floor = end-init
            wall = min(height[init], height[end])
            area = floor*wall
            if area > maxArea:
                maxArea = area
            if height[init] < height[end]:
                init += 1
            elif height[init] >= height[end]:
                end -= 1
        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
