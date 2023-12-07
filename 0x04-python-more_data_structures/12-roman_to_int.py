#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result, prev_value = 0, 0
    for c in roman_string:
        value = roman_d[c]
        result += value
        if value > prev_value:
            result -= prev_value * 2
        prev_value = value
    return result
