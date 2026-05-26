def list_operations():
    n = [3, 1, 2, 4, 5]
    n.insert(0, 0)
    print(n)
    n.append(6)
    print(n)
    del n[len(n) - 1]  # remove last element
    print(n)
    n.sort()
    print(n)


def dict_operations():
    people = {
        "name1": 10,
        "name2": 20,
        "name3": 30,
    }
    print(people)
    people.setdefault("name4", 50)
    print(people)
    people["name1"] = 40
    print(people)
    del people["name4"]

    for key, values in people.items():
        print(key, values)


def set_operations():
    set1 = {"bob", "alice", "jack"}
    set2 = {"jetha", "daya", "bob"}
    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)


def tuple_demo():
    image_shape = (3, 224, 224)
    channels, height, width = image_shape
    print(channels, height, width)
    # cannot modify tuples as they are immutable


def word_frequency(text):
    t = str(text).split(" ")
    value_dict = {}
    for i in t:
        key = i.lower()
        if value_dict.get(key) is not None:
            value_dict[key] += 1
        else:
            value_dict.setdefault(key, 1)
    return value_dict


def remove_duplicates(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    return temp


def tokenize(text):
    temp = str(text).split(" ")
    vocab = {}
    encoded = []

    for i in temp:
        key = i.lower()
        if key not in vocab:
            vocab[key] = len(vocab)
        encoded.append(vocab[key])
    return encoded


# print(list_operations())
# print(dict_operations())
# print(set_operations())
# print(tuple_demo())
# print(word_frequency("the cat sat on the mat the cat"))
# print(remove_duplicates([1,1,2,3,4]))
print(tokenize("the cat sat on the mat the cat"))
