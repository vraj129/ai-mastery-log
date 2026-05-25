def fizz_buzz():
    n = 30
    outputList = []
    for i in range(n + 1):
        outPutStr = ""
        if i % 3 == 0 and i % 5 == 0:
            outPutStr = "FizzBuzz"
        elif i % 3 == 0:
            outPutStr = "Fizz"
        elif i % 5 == 0:
            outPutStr = "Buzz"
        else:
            outPutStr = str(i)
        outputList.append(outPutStr)

    print(outputList)


def reveres_str():
    strV = "String to reverse"
    print(strV[::-1])


def mx_list():
    li = [1, 2, 3, 4, 5]
    max = 0
    for i in li:
        if max < i:
            max = i
    print(max)


def count_vowels():
    vowels = ['a', 'e', 'i', 'o', "u"]
    strV = "This is a string with some vowels"
    val_dict = {}
    for i in strV:
        if i.lower() in vowels:
            if val_dict.get(i) is None:
                val_dict.setdefault(i, 1)
            else:
                val_dict[i] += 1

    print(val_dict)

def is_prime():
    n = 8
    isPrime = True
    for i in range(2,n):
        if n % i == 0:
            isPrime = False
    print(isPrime)


# print(fizz_buzz())
# print(reveres_str())
# print(mx_list())
# print(count_vowels())
print(is_prime())
