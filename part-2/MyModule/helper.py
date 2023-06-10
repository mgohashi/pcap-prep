import re

def remove_vowels(my_str: str) -> str:
    return re.sub('[aeiou]', '', my_str)

def find_vowels(my_str: str) -> list:
    return re.findall("[aeiou]", my_str)

def __hidden():
    pass