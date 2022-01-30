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


# My test dictionary
# main_list = [{'A': 112, 'B': 922, 'C': 100, 'D': 45}, {'A': 11, 'B': 73, 'C': 1001}, {'A': 300}]
# Creating empty list for Task1.
main_list = []

# In list will be inserted from 2 to 10 dictionaries.
for i in range(random.randint(2, 10)):
    # In each random dictionary will be appended to the list
    main_list.append(generating_random_dict())
print(main_list)

# Creating dictionary which will include final result. As a start - saving first dictionary from list to it.
final_dict = main_list[0]
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

print(final_dict)
print('Thanks for your time again :)')
