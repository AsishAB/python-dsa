MAX_HASH_TABLE_SIZE = 4096
data_list = [None] * MAX_HASH_TABLE_SIZE


# Hashing algorithm
# Step 1 - Iterate over the string, character by character
# Step 2 - Convert each character to a number using Python's built-in ord() function
# Step 3 - Add the numbers, obtained from each character, to obtain the hash for the entire string
# Step 4 - Take the reminder of this sum, with the Maximum size of the data list (MAX_HASH_TABLE_SIZE)

def get_index(data_list, a_string):
    result = 0
    for character in a_string:
        a_number = ord(character)
        result += a_number

    list_index = result % len(data_list)
    return list_index

def get_valid_index(data_list, key):
    # To avoid Key colision, example - in case of 'listen' and 'silent', both the hashes will be the same.
    # So, we get the next available empty key to store the value

    #Start with the index returned by get_index
    idx = get_index(data_list, key)
    while True:
        # Get the key-value pair stored at index
        kv = data_list[idx]

        # if kv is None, return the index
        if kv is None:
            return kv
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if idx == k: # Check if this logic is correct
            return kv
        
        # Move to the index
        idx += 1

        # Go back to the start, if you have reached the end of the array
        if idx == len(data_list):
            idx = 0



class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # Create a list of size `max_size` with all values as None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # Store the key-value pair at the right index
        self.data_list[idx] = key, value # Stores the key-value pair as a Tuple

    def find(self, key):
        # Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # Retrive the data stored in the key
        kv = self.data_list[idx]

        # Return the value, if key is found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # Find the index of the key using get_index
        idx = get_index(self.data_list, key)

        # Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
    

basic_table = BasicHashTable(1024)


basic_table.insert('Aakash', '9999099990')
basic_table.insert('Hemant', '9898989898')

print(basic_table.find('Aakash'))