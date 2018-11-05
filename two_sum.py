# https://leetcode.com/problems/two-sum/

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def two_sum(nums, target):
    dictionary = {num: index for index, num in enumerate(nums)}
    for index, num in enumerate(nums):
        second = dictionary.get(target - num, None)
        if not second is None and not index == second:
            return [index, second]

def testcases():
    print(two_sum(nums = [2, 7, 11, 15], target = 9))

if __name__ == '__main__':
    testcases()
