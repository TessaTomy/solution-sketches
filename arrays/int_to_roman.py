# int_to_roman.py
# Problem: Integer to Roman (LeetCode)
# Approach: Greedy subtraction using sorted dictionary of Roman symbols

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

        result = ""
        for value in sorted(roman_map.keys(), reverse=True):
            while num >= value:
                result += roman_map[value]
                num -= value
        return result
