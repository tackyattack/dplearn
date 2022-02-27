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
    x = [0] * len(a)  # feeler
    h = [0] * len(a)  # height map for feeler
    for i in range(1, len(a)-1):
        cur = a[i]
        l = a[i-1]
        r = a[i+1]
        # feeler that goes out to see how far it can trap
        for u in range(cur, l+1):
            z = 0
            for p in range(i, len(a)):
                if a[p] >= u:
                    z = p-i
                    break
            if z >= x[i]:
                x[i] = z
                h[i] = u
        print(i)
    print(x)
    print(h)
    # now go back and fill in lower areas
    i = 1
    g = [0] * len(a)
    total_count = 0
    while i < len(a)-1:
        if x[i] > 0:
            level = h[i]
            for p in range(i, i+x[i]):
                i = p
                g[i] = level - a[i]
                total_count = total_count + g[i]
        i = i + 1
    print(g)
    print(total_count)
    return total_count


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
