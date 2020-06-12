def check_input(input_list):
    """ Checks to see if user input is a list of numbers

    Parameters
    ----------
    input_list : list
        List to be checked whether it is a list of numbers
    Returns
    -------
    output: boolean
        False if input list is a list of numbers
        True if input list does not meet the conditions    
    """
    loop_condition = False

    # check if input list is longer than 2
    if len(input_list) <= 1:
        print("Error: input must be more than one number")
        loop_condition = True

    not_numbers = False

    # check if input list is all numbers
    for x in input_list:
        if not x.isdecimal():
            not_numbers = True
            loop_condition = True
    if not_numbers:
        print("Error: input may only be numbers")
        not_numbers = False
        loop_condition = True
    
    return loop_condition 


def change_to_int(input_list):
    """ Change all elements in list to ints

    Parameters
    ----------
    input_list : list
        List to be changed to int
    Returns
    -------
    output: list of ints
        converted list with same elements as ints   
    """
    output_list = []
    for x in input_list:
        output_list.append(int(x))
    return output_list
    

def split(input_list):
    """ Helper function for sorting that recursively splits the list in half
        and calls other helper function to sort the elements

    Parameters
    ----------
    input_list : list
        List to be recursively split in half
    Returns
    -------
    output: list
        List that is sorted   
    """
    # if there is only one element in the list
    if len(input_list) == 1:
        print("cannot be split further: ", input_list)
        print()
        return input_list

    print("split in half: ", input_list)
    print()

    # get the middle point of the list
    mid = int(len(input_list) / 2)

    # split the list
    l = input_list[:mid]
    r = input_list[mid:]

    # recursively call the split function
    l_merge = split(l)
    r_merge = split(r)
    
    # call the function to merge lists and return the sorted list
    return merge(l_merge, r_merge)


def merge(l_merge, r_merge):
    """ helper function for sorting that will take elements of two lists and 
        compare their elements in order to sort them

    Parameters
    ----------
    input_list : list1, list2
        Lists to be sorted
    Returns
    -------
    output: list
        sorted list  
    """
    merged = []

    # while both lists still have elements
    while len(l_merge) != 0 and len(r_merge) != 0:
        l_elem = l_merge[0]
        r_elem = r_merge[0]

        # if the left element is larger than the right element
        if int(l_elem) > int(r_elem):
            # add the right element to the sorted list
            merged.append(r_elem)
            del r_merge[0]
        # else if the right element is larger than the left element
        else:
            # add the left element to the sorted list
            merged.append(l_elem)
            del l_merge[0]

    # while the left list is not empty but the right list is empty
    while len(l_merge) != 0:
        # add the left element to the sorted list
        merged.append(l_merge[0])
        del l_merge[0]

    # while the left list is not empty but the right list is empty
    while len(r_merge) != 0:
        # add the right element to the sorted list
        merged.append(r_merge[0])
        del r_merge[0]

    print("merged: ", merged)
    print()
    
    # return the sorted list
    return merged