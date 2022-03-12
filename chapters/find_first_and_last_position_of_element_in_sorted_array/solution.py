import bisect
import pytest

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, bisect.bisect_left(nums, target + 1) - 1]

@pytest.mark.parametrize(
    'nums, target, expected_output', [
        ([1], 1, [0, 0]),
        ([1], 8, [-1, -1]),
        ([5,7,7,8,8,10], 8, [3, 4]),
        ([5,7,7,8,8,10], 6, [-1, -1]),
        ([], 0, [-1, -1])
    ]
)
def testcases(nums, target, expected_output):
    assert Solution().searchRange(nums, target) == expected_output
