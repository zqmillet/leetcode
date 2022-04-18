import pytest

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        pass

@pytest.mark.parametrize(
    'obstacleGrid, expected_output', [
        ([[0,0,0],[0,1,0],[0,0,0]], 2),
        ([[0,1],[0,0]], 1),
        ([[0,0,0,0,1],[0,1,1,0,1],[0,0,1,0,0],[1,0,0,0,0]], 3),
    ]
)
def testcases(obstacleGrid, expected_output):
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == expected_output
