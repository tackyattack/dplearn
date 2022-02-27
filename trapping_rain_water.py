# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by
# array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
# (blue section) are being trapped.

# Input: height = [4,2,0,3,2,5]
# Output: 9

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

import unittest

# unoptimized solution
# TODO: apply DP


def find_water(a):
    total_trapped = 0
    map_size = len(a)
    x = [0] * map_size
    for i in range(1, map_size-1):
        lmax = 0
        rmax = 0
        for j in range(0, i):
            lmax = max(lmax, a[j])
        for j in range(i, map_size):
            rmax = max(rmax, a[j])
        x[i] = max(min(lmax, rmax) - a[i], 0)
        total_trapped = total_trapped + x[i]
    print(x)
    print(total_trapped)
    return total_trapped


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, find_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_2(self):
        self.assertEqual(9, find_water([4, 2, 0, 3, 2, 5]))

    def test_3(self):
        self.assertEqual(4, find_water([1, 0, 0, 0, 0, 1]))

    def test_4(self):
        self.assertEqual(9, find_water([2, 0, 0, 1, 0, 0, 2]))

    def test_5(self):
        self.assertEqual(1, find_water([4, 2, 3]))

    def test_6(self):
        self.assertEqual(2, find_water([2, 0, 0, 1]))

    def test_7(self):
        self.assertEqual(2, find_water([2, 0, 2]))


if __name__ == '__main__':
    unittest.main()
