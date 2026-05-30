def count_words(text):
    return len(text.strip().split())


def count_chars(text):
    return len(text), len(text.replace(" ", ""))


def word_frequency(text):
    word_dict = {}
    for i in text.split():
        key = i.lower()
        if key in word_dict:
            word_dict[key] += 1
        else:
            word_dict[key] = 1
    return word_dict


def most_common_word(text):
    word_dict = word_frequency(text)
    word = ""
    most_frequent = 0
    for key, values in word_dict.items():
        if values > most_frequent:
            word = key
            most_frequent = values
    return word, most_frequent


def count_sentences(text):
    li = [x for x in text.split(".") if x.strip()]
    return len(li)


def analyze(text):
    print("===== TEXT ANALYSIS REPORT =====")
    count_char = count_chars(text)
    print(f"Word count: {count_words(text)}")
    print(f"Char count: {count_char[0]} (with spaces)")
    print(f"Char count: {count_char[1]} (without spaces)")
    print(f"Sentences: {count_sentences(text)}")
    res = most_common_word(text)
    print(f"Most common word: {res[0]} (appears {res[1]} times)")
    print("=================================")


sentence = "Python is a great language. Python is used in AI and data science. Learning Python every day makes you better. Every day is a new opportunity to learn something new."
analyze(sentence)
