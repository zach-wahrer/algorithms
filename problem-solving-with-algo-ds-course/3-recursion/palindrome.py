def is_palindrome(string):
    print(remove_non_alpha(string))
    print(reverse_string(string))
    return remove_non_alpha(string) == reverse_string(string)


def remove_non_alpha(string):
    if len(string) == 1:
        if not string.isalpha():
            return ""
        return string.lower()
    moves = 0
    while not string[moves].isalpha():
        moves += 1
    return string[moves].lower() + remove_non_alpha(string[moves + 1:])


def reverse_string(string):
    if len(string) == 1:
        if not string.isalpha():
            return ""
        return string.lower()
    moves = -1
    while not string[moves].isalpha():
        moves -= 1
    return string[moves].lower() + reverse_string(string[:len(string) - abs(moves)])


print(is_palindrome('Go hang a salami; I’m a lasagna hog.'))
