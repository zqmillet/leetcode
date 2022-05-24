from typing import List
from bisect import bisect_left
from itertools import combinations
from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        min_distance = inf
        result = None
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:

        for x, y in combinations(nums, 2):
            delta = target - x - y

            index = bisect_left(nums, delta)

            z1 = nums[index] if index < len(nums) else nums[-1]
            z2 = nums[index + 1] if index + 1 < len(nums) else z1

            distance_1, distance_2 = abs(x + y + z1 - target), abs(x + y + z2 - target)

            if distance_1 < min_distance:
                min_distance = distance_1
                result = x + y + z1
            elif distance_2 < min_distance:
                min_distance = distance_2
                result = x + y + z2

        return result

import pytest

@pytest.mark.parametrize(
    'nums, target, expected_result', [
        ([-1,2,1,-4], 1, 2),
        ([0,0,0], 1, 0),
        ([1, 1, -1], 2, 1),
    ]
)
def test(nums, target, expected_result):
    assert Solution().threeSumClosest(nums, target) == expected_result
