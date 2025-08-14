def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_chars(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in char_dict:
                char_dict[lower_char] = 1
            else:
                char_dict[lower_char] += 1
    return char_dict


def generate_report(char_counts):

    list_of_dicts = [
        {"char": character, "num": occurence_count}
        for character, occurence_count in char_counts.items()
    ]

    def sort_on(item):
        return (-item["num"], item["char"])

    list_of_dicts.sort(key=sort_on)

    # ordered_dict = {d["char"]: d["num"] for d in list_of_dicts}
    return list_of_dicts
