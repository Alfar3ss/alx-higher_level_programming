def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if i > 0 and roman_numerals[roman_string[i]] > roman_numerals[roman_string[i - 1]]:
            total += roman_numerals[roman_string[i]] - 2 * roman_numerals[roman_string[i - 1]]
        else:
            total += roman_numerals[roman_string[i]]

    return total
