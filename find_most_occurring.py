sentence = "This is a common interview question"


def get_most_occurring_char(string):
    clear_whitespaces = string.replace(" ", "").lower()
    return clear_whitespaces


print(get_most_occurring_char(sentence))
