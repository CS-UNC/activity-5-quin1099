def twenty_or_more(file):
    words_20 = []
    with open(file, "r") as f:
        for line in f:
            for word in line.split():
                if len(word) > 20:
                    words_20.append(word)
    return words_20

def has_no_e(word):
    return 'e' not in word and 'E' not in word

def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

def all_uses_only(file, letters):
    valid_words = []
    with open(file, "r") as f:
        for line in f:
            for word in line.split():
                if uses_only(word, letters):
                    valid_words.append(word)
    return valid_words