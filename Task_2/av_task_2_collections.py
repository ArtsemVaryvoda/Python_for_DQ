# 2nd Homework
# 1. create a list of random number of dicts (from 2 to 10)
# 1.1 dictionaries random numbers of keys should be letter.
# 1.2 dictionaries values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value

import random
import string


def generating_random_dict():
    i = 0
    rand_dict = {}
    while i < random.randint(2, 10):
        rand_dict[random.choice(string.ascii_letters)] = random.randint(0, 100)
        i += 1
    return rand_dict


dict_1 = generating_random_dict()
dict_2 = generating_random_dict()

print(dict_1)
print(dict_2)

final_dict = dict(dict_1, **dict_2)

print(final_dict)
