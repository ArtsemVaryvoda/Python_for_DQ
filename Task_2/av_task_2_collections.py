# 2nd Homework
# 1. create a list of random number of dicts (from 2 to 10)
# 1.1 dictionaries random numbers of keys should be letter.
# 1.2 dictionaries values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value

# Library used to generate random integers
import random
# Library used to get ascii_lowercase letters
import string


# Method to create random dictionary which will be inserted into list.
def generating_random_dict():
    # System int which will be used for iterations in while loop.
    it = 0
    # Creating empty dictionary in which random values will be inserted.
    rand_dict = {}
    # While loop which will iterate between 2 and 10 times based on random.
    while it < random.randint(2, 10):
        # Inserting values. Key - random lowercase. Value - random integer.
        # For keys, I chose lowercase to prevent situations when we will have a and A. It is different values from
        # Python view, while for human A and a could look same way. Just for convenience.
        rand_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        # Increasing i by 1 for while loop. When i will reach random value loop will end.
        it += 1
    # Returning random dictionary (with 2-10 elements) which was created.
    return rand_dict


# Creating empty list for Task1.
main_list = []

# In list will be inserted from 2 to 10 dictionaries.
for i in range(random.randint(2, 10)):
    # In each random dictionary will be appended to the list
    main_list.append(generating_random_dict())

# Oleksandr  test dictionary
# main_list = [{'a':1,'b':3,'c':3,'d':4},{'b':3,'c':4,'e':5},{'b':2,'d':3,'f':7},{'b':3,'h':0}]

print('Initial list is: ' + str(main_list))


# Method to save keys, existing values and indexes of the list. It is need to save indexes to understood from which
# dictionary (number) value was extracted, my first solution didn't allow to do this, so creating preliminary list.
def save_list_values_and_indexes(input_list):
    prel_dict = {}
    # Iterating through each dictionary of our main_list
    for i in range(len(input_list)):
        # Iterating through each key/value a pair of dictionary
        for key, value in main_list[i].items():
            # When key was not in preliminary list before - just insert it. i var will serve us as index
            if key not in prel_dict.keys():
                # Creating new key, adding value and index of it. +1 because i starts from 0, while in task we start
                # from one
                prel_dict[key] = [[value], [i]]
            # When key existing already - just appending element consisting of value and index.
            elif key in prel_dict.keys():
                # Value addition
                prel_dict[key][0].append(value)
                # Index addition
                prel_dict[key][1].append(i)
    return prel_dict


# Method to scan through preliminary dictionary, select max values, add _x postfix
def get_max_values_from_prel_dictionary(dict):
    # Creating empty dictionary to save results
    final_dict = {}
    # Iterating through all key/value pairs of preliminary dictionary
    for key, value in dict.items():
        # When for letter we have > 1 value - select max value
        if len(value[0]) > 1:
            # Saving max value into var because we will need it 2 times - for value itself and searching dict num
            max_val = max(value[0])
            # Adding _x postfix, where x is number of dictionary with max value
            key = key + '_' + str(value[1][value[0].index(max_val)])
            # Inserting key/value pair in final dictionary
            final_dict[key] = max_val
        # When value only one time across all dictionaries - simply insert it
        elif len(value[0]) == 1:
            # Inserting key/value pair in final dictionary
            final_dict[key] = value[0][0]
    return final_dict


# Getting preliminary list
prel_list = (save_list_values_and_indexes(main_list))
# Getting final_list and printing it
print('Final dictionary: ' + str(get_max_values_from_prel_dictionary(prel_list)))

'''
# Legacy code
# Variable used for controlling loop and with which dictionary from list we are currently comparing.
comp_with_lst_num = 1
# While loop to compare dictionaries. For example, we will compare 1 vs 2nd Then result of comparison of 1 and 2nd
# with 3rd. Then (1/2/3) vs 4th. Until all dictionaries will be compared.
while comp_with_lst_num < len(main_list):
    # Iteration through every key of dictionary. .copy() is used because during work with final_dict we need to change
    # some elements, and Python don't allow us to do it in for loop. .copy() solves problem
    for key in final_dict.copy():
        # In case if keys will be the same a == a for example we will compare values. I used key[0] because it could be
        # situation when after comparing 1st and 2nd, and in both dictionaries will be a with different values. For
        # example in dictionary 1 it will be higher. So in the result in final_dict will be value a_1. And when we will
        # compare with other dictionaries if condition won't match, a_1 != 1. But using key[0] we will always get a.
        if key[0] in main_list[comp_with_lst_num]:
            # Case when value in 1st dictionary higher than in the 2nd.
            if final_dict[key] > main_list[comp_with_lst_num][key[0]]:
                print(str(final_dict[key]) + ' is higher than ' + str(main_list[comp_with_lst_num][key[0]])
                      + ' for key ' + str(key[0]))
                # Removing key/value from second dictionary.
                main_list[comp_with_lst_num].pop(key[0])
                # Renaming key of the first dictionary from x to x_1, where x is letter. Number is dict_num
                final_dict[key[0] + '_' + str(comp_with_lst_num)] = final_dict.pop(key)
            # Case when value in 2nd dictionary higher than in the 1st.
            elif final_dict[key] < main_list[comp_with_lst_num][key[0]]:
                print(str(final_dict[key]) + ' is lower than ' + str(main_list[comp_with_lst_num][key[0]])
                      + ' for key ' + str(key[0]))
                # Replacing value from 2nd dictionary to 1st because 2nd is greater.
                final_dict[key] = main_list[comp_with_lst_num][key[0]]
                # Removing key/value pair from 2nd dictionary.
                main_list[comp_with_lst_num].pop(key[0])
                # Renaming key of the first dictionary from x to x_, where x is letter. Number is dict_num
                final_dict[key[0] + '_' + str(comp_with_lst_num + 1)] = final_dict.pop(key)
            # Case when values of key is the same, and we shouldn't change any values.
            elif final_dict[key] == main_list[comp_with_lst_num][key[0]]:
                print(key + ' exists in both dictionaries with same values')
                # Replacing key/value from 2nd dictionary
                main_list[comp_with_lst_num].pop(key[0])
    # Merging in final dictionary 2nd dictionary. All values with same keys was proceeded already, so only left to
    # insert keys which are not common between dictionaries.
    final_dict = final_dict | main_list[comp_with_lst_num]
    # Adding 1 for our system variable to control loop.
    comp_with_lst_num += 1
'''
