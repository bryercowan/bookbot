def sort_on(dict):
    return dict["num"]

def sorted_letter_list(letters):
    sorted_list = []
    for l in letters:
        sorted_list.append({"char": l, "num": letters[l]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


def get_letter_count(string):
    letters = {}
    for c in string:
        cl = c.lower()
        if cl in letters:
            letters[cl] += 1
        else:
            letters[cl] = 1
    return letters

def get_word_count(string):
    arr = string.split()
    return len(arr)
