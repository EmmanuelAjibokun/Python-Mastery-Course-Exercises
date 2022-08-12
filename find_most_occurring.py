sentence = input(
    "Input your sentence, let's find the most occurring character: ")


def sort_char_by_occurence(string):
    clear_whitespaces = string.replace(" ", "").lower()
    # print(clear_whitespaces)
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
        frequency.append(len(sorted_char[item]))
    sorted_freq = sorted(frequency)

    # print(sorted_freq)

    for item in sorted_char:
        if len(sorted_char[item]) == sorted_freq[-1]:
            return f"\n=> The most occurring character in: '{sentence}' is \"{item}\"\n"

    # return sorted_char


print(get_most_occurring_char())
