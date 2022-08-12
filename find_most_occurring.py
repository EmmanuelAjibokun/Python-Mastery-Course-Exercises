sentence = "This is a common interview question"


def get_most_occurring_char(string):
    clear_whitespaces = string.replace(" ", "").lower()
    print(clear_whitespaces)
    sort_character = {}
    for char in clear_whitespaces:
        if char in sort_character:
            sort_character[char] = sort_character[char] + char
            print(f"character: {char} exist in sort_charcter")
        else:
            sort_character[char] = char

    return sort_character


print(get_most_occurring_char(sentence))
