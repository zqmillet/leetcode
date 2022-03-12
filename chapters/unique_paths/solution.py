import pytest
from math import factorial

class Solution(object):
    def ncr(self, n, r):
        return factorial(n) // factorial(r) // factorial(n - r)

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.ncr(m + n - 2, m - 1)

@pytest.mark.parametrize(
    'm, n, expected_output', [
        (3, 7, 28),
        (3, 2, 3),
        (3, 3, 6),
    ]
)
def testcases(m, n, expected_output):
    assert Solution().uniquePaths(m, n) == expected_output
