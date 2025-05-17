/**
 * Solution class for converting an integer to a Roman numeral.
 */

#include <string>
#include <vector>
#include <map>

class Solution {
 public:
  string intToRoman(int num) {
    string roman_str;
    vector<int> potencies = {1000, 100, 10, 1};
    map<int, string> roman_equivalences = {
        {1, "I"},
        {5, "V"},
        {10, "X"},
        {50, "L"},
        {100, "C"},
        {500, "D"},
        {1000, "M"}
    };

    for (int power : potencies) {
      int digit = num / power;
      int power_digit = digit * power;
      num = num % power;

      if (digit == 0) continue;
      if (roman_equivalences.count(power_digit)) {
        roman_str += roman_equivalences[power_digit];
        continue;
      }
      if (digit == 4 || digit == 9) {
        string prefix = roman_equivalences[power];
        roman_str += prefix + roman_equivalences[power * (digit + 1)];
        continue;
      }
      if (digit > 5) {
        roman_str += roman_equivalences[power * 5];
        digit -= 5;
      }
      roman_str += string(digit, roman_equivalences[power][0]);
    }
    return roman_str;
  }
};
