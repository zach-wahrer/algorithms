def reverse_string(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse_string(string[:len(string) - 1:])


print(reverse_string('reverse this'))
