"""424. Longest Repeating Character Replacement
Medium
Topics
Companies

You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        right = 0

        count_letters = defaultdict(int)
        max_letter_count = 0

        out = 0

        while right < len(s):
            length = right - left + 1
            count_letters[s[right]] += 1
            max_letter_count = max(count_letters.values())

            if length - max_letter_count <= k:
                out = max(out, length)
            else:
                count_letters[s[left]] -= 1
                left += 1

            right += 1
        
        return out

def main():
    test = Solution()
    print(test.characterReplacement("ABAB", 2))

if __name__ == "__main__":
    main()
