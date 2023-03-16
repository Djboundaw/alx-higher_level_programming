#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max = 0
    my_key = ""
    for i in a_dictionary.keys():
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            my_key = i
    return (my_key)
