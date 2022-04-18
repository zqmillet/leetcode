from typing import List

class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def _function(candidates, target):
            results = set()

            if target in candidates:
                results.add((target,))

            for index, item in enumerate(candidates):
                for result in _function(candidates[:index] + candidates[index + 1:], target - item):
                    if item > result[0]:
                        continue
                    results.add((item, *result))

            return results
        return list(map(list, _function(candidates, target)))

import pytest

@pytest.mark.parametrize(
    'candidates, target, expected_result', [
        (
            [10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]
        ),
        (
            [2,5,2,1,2], 5, [[1,2,2], [5]]
        ),
        (
            [], 5, []
        ),
    ]
)
def test(candidates, target, expected_result):
    print(Solution().combinationSum2(candidates, target))
    # assert Solution().combinationSum2(candidates, target) == expected_result
