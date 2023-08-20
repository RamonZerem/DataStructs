def dictionary_basic():
    """
    Some simple operations with dictionary
    """
    empty_dict = {}  # initialize an empty dictionary
    super_heroes = {"Spider-man": "Peter Parker", "Flash": "Barry allen"}  # initialize a dictionary
    print(super_heroes["Spider-man"])  # Access value by key
    del super_heroes["Flash"]  # Delete pair
    print("Flash" in super_heroes)  # Print if key in the dictionary
    super_heroes["Batman"] = "Bruce Wayne"  # Add a pair to the dictionary
    for hero in super_heroes:
        print(super_heroes[hero], " is the real name of ", hero)


def basic_list_comprehension(n):
    """
    Initialize a list with number 0-n in 1 line
    :param n: The list range
    :return: The list you created
    """

    return [i for i in range(n)]


def square_list_comprehension(n):
    """
    initialize a list with number 0-n in square in 1 line
    :param n: The list range
    :return: The list you created
    """
    return [i**2 for i in range(n)]


def seven_BOOM_list_comprehension(n):
    """
    initialize a list with number 0-n, in which every multiple of 7 is replaced with BOOM in 1 line
    :param n: The list range
    :return: The list you created
    """
    return ["BOOM" if i % 7 == 0 else i for i in range(n)]


def not_in_string_list_comprehension(original_str, chars_to_delete):
    """
    initialize a list with the characters from the original_str that are not in the chars_to_delete
    :param original_str: The original string
    :param chars_to_delete: The string to not use in the list
    :return: The list you created
    """
    return [letter for letter in original_str if letter not in chars_to_delete]
