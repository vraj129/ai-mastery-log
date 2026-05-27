def square_num():
    for i in range(1, 11):
        print(i ** 2)
    li = [x ** 2 for x in range(1, 11)]
    print(li)


def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
    li = [x for x in range(1, 21) if x % 2 == 0]
    print(li)


def dict_comp():
    words = ["hello", "ai", "python", "model"]
    dict = {}
    for word in words:
        key = word.lower()
        dict[key] = len(word)
    print(dict)

    dict_comprehension = {key: len(key) for key in words}
    print(dict_comprehension)


def generator_comp():
    gen = (x * x for x in range(1000000))
    it = iter(gen)
    for _ in range(5):
        print(next(it))


def clean_string():
    texts = [" Hello ", "WORLD", "", " ai ", "Python"]
    li = [x.lower().strip() for x in texts if x.strip()]
    print(li)


def tokenize(text):
    temp = str(text).split(" ")
    vocab = {}

    for i in temp:
        key = i.lower()
        if key not in vocab:
            vocab[key] = len(vocab)

    encoded = [vocab[key.lower()] for key in temp]

    decoded_dict = {id1: word for word, id1 in vocab.items()}
    decoded_list = [decoded_dict[id1] for id1 in encoded]

    return {
        "vocab": vocab,
        "encoded": encoded,
        "decoded": decoded_list
    }


# print(square_num())
# print(even_numbers())
# print(dict_comp())
# print(generator_comp())
# print(clean_string())
print(tokenize("the cat sat on the mat the cat"))