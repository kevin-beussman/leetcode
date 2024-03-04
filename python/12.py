"""12. Integer to Roman
Medium
Topics
Companies

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= num <= 3999

"""

#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class Solution:
    def intToRoman(self, num: int) -> str:
        map_int_to_roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        answer = ""
        while num:
            biggest_key = self._get_biggest_less_than_threshold(map_int_to_roman.keys(), num)
            answer += map_int_to_roman[biggest_key]
            num -= biggest_key
        return answer

    @staticmethod
    def _get_biggest_less_than_threshold(list_of_nums, threshold):
        biggest = 0
        for num in list_of_nums:
            if num <= threshold:
                biggest = max(biggest, num)
        return biggest if biggest > 0 else None


def main():
    test = Solution()
    print(test.intToRoman(444))

if __name__ == "__main__":
    main()
