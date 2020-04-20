word_list = ['cat', 'dog', 'rabbit']
letter_list = []

for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)

letter_list2 = set([letter for word in word_list for letter in word])

print(letter_list)
print(letter_list2)
