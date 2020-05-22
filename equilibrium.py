'''
Intro:

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].


'''


def solution(A):
    # the idea to solve in O(N) is that you get the first value from the array A[0] and sum all the remaining values with
    # python sum function: which is O(N)
    # then from 1 to N (size of A) we verify if the |left-right| is smaller the smallest difference and increase left and decrease right
    # We get O(N) + O(N) = O(N)

    if len(A) == 2:

        return abs(A[0]-A[1])

    minValue = float("inf")
    leftValue = A[0]
    rightValue = sum(A[1:])

    for i in range(1, len(A)):
        if abs(leftValue - rightValue) < minValue:
            minValue = abs(leftValue-rightValue)
        leftValue += A[i]
        rightValue -= A[i]

    return minValue


# Score of solution: 100%
# time: 10 min
