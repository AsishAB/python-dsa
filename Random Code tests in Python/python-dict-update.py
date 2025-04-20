policies = [
    {"key1": "Value1"},
    {"key2": "Value2"},
    {"key3": "Value3"},
    {"key4": "Value4"}
]

def add_new_key(policy):
    for policy in policies:
        policy['key5'] = 'value5'
    

print(policies)
    