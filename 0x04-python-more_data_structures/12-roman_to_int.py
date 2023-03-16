#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string == "":
        return 0
    value = 0
    length = len(roman_string)
    rom_dico = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
     }
    for i in range(length):
        if rom_dico.get(roman_string[i], 0) == 0:
            return 0
        if (length - 1) and rom_dico[roman_string[i]] < ro[roman_string[i + 1]]):
             num += rom_dico[roman_string[i]] * -1

        else:
            num += rom_dico[roman_string[i]]
        return (nnum)
