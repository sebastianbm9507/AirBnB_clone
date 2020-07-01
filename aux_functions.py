"""Modulo to auxiliar functions
"""

import console


def list_to_dict(str_list):
    """ list to dict """
    new_word = ""
    for letra in str_list:
        if letra not in '[}"{:]':
            new_word = new_word + letra
    # (i.e) -> '', 'key', 'value' 🔐
    new_word2 = ""
    for letra in new_word:
        if letra not in '\',':
            new_word2 = new_word2 + letra
    #  (i.e) -> key value 🔐
    list_two = new_word2.split()
    dictOfWords = {
        list_two[i]: list_two[i + 1] for i in range(0, len(list_two), 2)
        }
    # (i.e)-> {'key': 'value'} 🔐
    return dictOfWords
