MAX_HASH_TABLE_SIZE = 4096
data_list = [None] * MAX_HASH_TABLE_SIZE


# Hashing algorithm
# Step 1 - Iterate over the string, character by character
# Step 2 - Convert each character to a number using Python's built-in ord() function
# Step 3 - Add the numbers, obtained from each character, to obtain the hash for the entire string
# Step 4 - Take the reminder of this sum, with the Maximum size of the data list (MAX_HASH_TABLE_SIZE)

def get_index(a_string, data_list):
    result = 0
    for character in a_string:
        a_number = ord(character)
        result += a_number

    list_index = result % len(data_list)
    return list_index

