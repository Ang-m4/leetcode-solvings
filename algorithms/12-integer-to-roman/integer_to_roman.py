"""
Module for converting integers to Roman numerals.

This module contains a Solution class with a method intToRoman that converts
an integer to its corresponding Roman numeral representation.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_str = ""
        potencies = [1000, 100, 10, 1]
        roman_equivalences = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }

        for power in potencies:
            # Gets the digit at the current power (e.g. 4532, power=1000 -> 4)
            digit = num // power
             # Gets the value at the current power (e.g. 4*1000=4000)
            power_digit = digit * power
            # Removes the processed digit from num (e.g. 4532 % 1000 = 532)
            num = num % power

            # Skip if there is no digit at this power
            if digit == 0:
                continue
            # Direct mapping exists (e.g. 1000, 500, 100, etc.)
            if power_digit in roman_equivalences:
                roman_str += roman_equivalences[power_digit]
                continue
            # Handle subtractive notation (e.g. 4=IV, 9=IX, 40=XL, etc.)
            if digit in (4, 9):
                prefix = roman_equivalences[power]
                roman_str += (prefix + roman_equivalences[power * (digit + 1)])
                continue
             # For digits 6-8, add the '5' symbol and repeat the '1' symbol as needed
            if digit > 5:
                roman_str += roman_equivalences[power * 5]
                digit -= 5

            # Append the '1' symbol as many times as needed
            roman_str += roman_equivalences[power] * digit
        return roman_str
