
sentence = "mynameismahhy"
dict = {'tee': 'a', 'h': 'hech', 'i': 't', 's': 's', 'a': 'a'}
iterable = "t"

for char in sentence:
    if char in dict:    # the "in" operator compares against the dictionary keys not values
        print(dict[char], "this", "=> ", char)
    else:
        print(char, ": that does not exist")
