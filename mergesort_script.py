import sys
sys.path.append('../')

from my_module.mergesort_functions import check_input
from my_module.mergesort_functions import change_to_int
from my_module.mergesort_functions import merge
from my_module.mergesort_functions import split

loop_condition = True

# loop while trying to get to get correct user input
while loop_condition:

    # prompt to get user input
    user_input = input("Please enter a list of numbers separated my a space: ")

    # split user input into list
    user_input_list = user_input.split()

    # check whether user input is correct
    loop_condition = check_input(user_input_list)

# change user input to a list on ints
user_list = change_to_int(user_input_list)

print("Preforming mergesort on list")
print("Process of sorting:")

# call functions for mergesort and save sorted list
merged_list = split(user_list)

print("Sorted list:", merged_list)