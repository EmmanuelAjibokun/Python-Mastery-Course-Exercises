sentence = "This is a common interview question"


def sort_char_by_occurence(string):
    clear_whitespaces = string.replace(" ", "").lower()
    print(clear_whitespaces)
    sorted_character = {}
    for char in clear_whitespaces:
        if char in sorted_character:
            sorted_character[char] = sorted_character[char] + char
        else:
            sorted_character[char] = char

    return sorted_character


def get_most_occurring_char():
    sorted_char = sort_char_by_occurence(sentence)
    frequency = []
    for item in sorted_char:
        print(item, "> length: ", len(sorted_char[item]))
        frequency.append(sorted_char[item])

    print(frequency)

    return sorted_char


print(get_most_occurring_char())
