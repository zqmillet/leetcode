import pytest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            second = dictionary.get(target - num, None)
            if not second is None and not index == second:
                return [index, second]
        return []

@pytest.mark.parametrize(
    'nums, target, expected_output', [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
)
def testcases(nums, target, expected_output):
    assert Solution().twoSum(nums, target) == expected_output
