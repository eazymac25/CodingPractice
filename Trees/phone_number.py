"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

[image from leetcode see link in readme]

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want
"""

class Solution(object):
    digit_map = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
        0: ""
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        The idea is that as you go through the digits
        there are multiple pathways that begin to fan out.
        This indicates a tree structure of digits, so a dfs
        was used to construct all combinations.
        """
        if len(digits) == 0:
            return []
        return self.dfs(digits, curr="", results=[])

    def dfs(self, digits, curr="", results=[]):
        if len(digits) == 0:
            results.append(curr)
            return
        digit = int(digits[0])
        possible = self.digit_map.get(digit)
        for letter in possible:
            n_curr = curr + letter
            self.dfs(digits[1:], curr=n_curr, results=results)
        return results