my_list = ['mummy', 'hannah','murder for a jar of red rum','mom','seagull','tomato','no lemon, no melon','some men interpret nine memos','madam']

def is_palindrome(item):
    # Remove spaces and puntuation, lowecase everthing
    cleaned = ''.join(c.lower() for c in item if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Test the function with each item in the list
for item in my_list:
    if is_palindrome(item):
        print(f"'{item}' is palindrome")
    else:
        print(f"'{item}' is not a palindrome")
        
        