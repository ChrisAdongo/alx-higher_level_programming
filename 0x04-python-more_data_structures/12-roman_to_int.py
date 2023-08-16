#!/usr/bin/python3
def to_subtract(my_num):
    """Converts a Roman numeral to an integer."""

    to_sub = 0
    k = max(my_num)

    for n in my_num:
        if k > n:
            to_sub += n

    return (k - to_sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_keys = list(rom_n.keys())

    num = 0
    bot_num = 0
    my_num = [0]

    for ch in roman_string:
        for r_num in my_keys:
            if r_num == ch:
                if rom_n.get(ch) <= bot_num:
                    num += to_subtract(my_num)
                    my_num = [rom_n.get(ch)]
                else:
                    my_num.append(rom_n.get(ch))

                bot_num = rom_n.get(ch)

    num += to_subtract(my_num)

    return (num)
