import random

# First task of the Python for Data Quality program.
# Task is
# 1 - create list of 100 random numbers from 0 to 1000
# 2 - sort list from min to max (without using sort())
# 3 - calculate average for even and odd numbers
# 4 - print both average result in console

# Task1 - Create list of 100 random numbers from 0 to 1000

# Creating int variable which will be used for while loop to count sequence number of the cycle
x = 0

# Creating empty list to store 100 random numbers
one_hundred_rand_num = []

# Loop which will execute 100 times (from 0 till 99)
while x < 100:
    # In each iteration of the loop we are adding random number from 0 to 1000. Generated via random.randint\
    # Also import of random library was required
    one_hundred_rand_num.append(random.randint(0, 1000))
    # In each iteration of the loop adding 1 to x var. When x var will reach 100 while won't be met and loop will exit
    x = x + 1

# Check how many values list currently include. For debugging
# print("Currently list includes " + str(len(one_hundred_rand_num)) + " elements.")

# Also loop could be made by for loop in range (100)

# To sort list I choose bubble sorting. Ordinary method in which we are passing list. The downside is that sorting
# runs as many iterations as many numbers in the list.

# Defining function


def bubble(arr):
    # Saving length of the list into variable
    n = len(arr)
    # Traverse through all array elements
    for iteration in range(n):
        # Last iteration elements are already in place
        for j in range(0, n - iteration - 1):
            # traverse the array from 0 to n-iteration-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Calling bubble sorting function and passing our list in it.


bubble(one_hundred_rand_num)
# For debugging to see that bubble sorting actually works
# print("Sorted array is:")
# for i in range(len(one_hundred_rand_num)):
#    print("%d" % one_hundred_rand_num[i]),

# Creating list for even numbers
even_numbers = []
# Creating list for odd numbers
odd_numbers = []

# Go through all list, iteration will run 100 times because it is 100 elements in our list
for i in one_hundred_rand_num:
    # Check if number is even. If it is (for example for 2 division remainder 0) - append it to even_numbers list
    if i % 2 == 0:
        even_numbers.append(i)
    # If number is not even - it is odd! Append odd value to the list
    else:
        odd_numbers.append(i)

# For debugging to see that even/odd numbers lists include only required numbers
# print("Even numbers list: " + str(even_numbers))
# print("Odd numbers list: " + str(odd_numbers))

# Creating variables to get sum of all even/odd numbers
even_sum = 0
odd_sum = 0

# Add all values of even_numbers list during cycle
for i in even_numbers:
    even_sum = even_sum + i

# Add all values of odd_numbers list during cycle
for i in odd_numbers:
    odd_sum = odd_sum + i

# Task4 - print both average result in console
print("Average for even numbers: " + str(round(even_sum / len(even_numbers), 2)))
print("Average for odd numbers: " + str(round(odd_sum / len(odd_numbers), 2)))
print("Thank you for your time! :)")
