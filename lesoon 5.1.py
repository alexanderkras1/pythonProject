import string
import keyword

def starts_with_digit(a):
    if a and a[0].isdigit():
        return False
    return True

def invalid_chars(a):
    invalid_chars = string.punctuation.replace("_", "")
    for chars in a:
        if chars in invalid_chars or chars == " ":
            return False
    return True

def is_keyword(a):
    return not keyword.iskeyword(a)

def single(a):
    if "__" in a:
        return False
    return True

def contains_uppercase(a):
    for char in a:
        if char.isupper():
            return False
    return True

def valid(a):
    if not a:
        return False
    if not starts_with_digit(a):
        return False
    if not invalid_chars(a):
        return False
    if not is_keyword(a):
        return False
    if not single(a):
        return False
    if not contains_uppercase(a):
        return False
    return True

user_data = input("Введите вашу строку: ")
if valid(user_data):
    print("True")
else:
    print("False")
