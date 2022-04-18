code-block:: python

    from functools import lru_cache
    from typing import List

    class Solution(object):
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            candidates = tuple((item for item in sorted(candidates) if item <= target))

            @lru_cache
            def _function(candidates, target):
                results = set()

                if target in candidates:
                    results.add((target,))

                for index, item in enumerate(candidates):
                    for result in _function((*candidates[:index], *candidates[index + 1:]), target - item):
                        if item > result[0]:
                            continue
                        results.add((item, *result))

                return results
            return list(map(list, _function(tuple(candidates), target)))
