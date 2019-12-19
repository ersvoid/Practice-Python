import string
from random import randint


abc = list(string.ascii_lowercase)
ABC = list(string.ascii_uppercase)
num = list((range(1, 27)))

statement = ""


def encryption(word):
    word = word.lower()
    key = {}
    lst = []
    count = 0
    for w in word:
        x = randint(0, 2)
        y = randint(0, 25)
        index = abc.index(w)
        key[count] = [0, x, index, y]
        count += 1
        if x == 0:
            let = abc[y]
            lst.append(let)
        elif x == 1:
            let = ABC[y]
            lst.append(let)
        elif x == 2:
            let = str(num[y])
            lst.append(let)
    new = "".join(lst)
    value = [new, key]
    return value


def auto_encrypt(text):
    encrypted_lst = []
    key_lst = []
    lst = text.split()
    for word in lst:
        new = encryption(word)
        encrypted_lst.append(new[0])
        key_lst.append(new[1])
    phrase = " ".join(encrypted_lst)
    value = [phrase, key_lst]
    return value


def decryption(key):
    lst = []
    for i in range(0, len(key)):
        x = key[i][0]
        y = key[i][2]
        if x == 0:
            let = abc[y]
            lst.append(let)
        elif x == 1:
            let = abc[y]
            lst.append(let)
        elif x == 2:
            let = abc[y]
            lst.append(let)
    word = "".join(lst)
    return word


def auto_decrypt(key):
    lst = []
    word_count = len(key)
    for word in range(0, word_count):
        new = decryption(key[word])
        lst.append(new)
    phrase = " ".join(lst).capitalize() + "."
    return phrase


print(auto_decrypt(auto_encrypt(statement)[1]))
