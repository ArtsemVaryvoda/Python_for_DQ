import random
import string
import sys

def generate_random_dict():
    it = 0
    rand_dict = {}
    while it < random.randint(2, 10):
        rand_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        it += 1
    return rand_dict

def generate_list_of_dictionaries(min_dict, max_dict):
    if min_dict > max_dict or min_dict < 1:
        print("Number of dictionaries should be positive, min > 0 and min should be <= then max. Exiting the program")
        sys.exit()
    main_list = []
    for i in range(random.randint(min_dict, max_dict)):
        main_list.append(generate_random_dict())
    return main_list


def merge_list_values_and_indexes(input_list):
    prel_dict = {}
    for i in range(len(input_list)):
        for key, value in input_list[i].items():
            if key not in prel_dict.keys():
                prel_dict[key] = [[value], [i]]
            elif key in prel_dict.keys():
                prel_dict[key][0].append(value)
                prel_dict[key][1].append(i)
    return prel_dict


def get_max_values_from_prel_dictionary(dict):
    final_dict = {}
    for key, value in dict.items():
        if len(value[0]) > 1:
            max_val = max(value[0])
            key = key + '_' + str(value[1][value[0].index(max_val)])
            final_dict[key] = max_val
        elif len(value[0]) == 1:
            final_dict[key] = value[0][0]
    return final_dict


initial_list = generate_list_of_dictionaries(2, 10)
print('Initial list is: ' + str(initial_list))
prel_list = (merge_list_values_and_indexes(initial_list))
print('Final dictionary: ' + str(get_max_values_from_prel_dictionary(prel_list)))