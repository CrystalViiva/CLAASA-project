My_list = ["mummy", "hannah", "murder for a jar of red rum", "mom", "seagull", "tomato", "no lemon", "no melon", "some men interpret nine memos", "madam"]
# using for loop for each item on My_list
for item in My_list:
#    stripping punctuation and spaces to prevent them from breaking the reverse string logic.
    edited = "".join(char for char in item if char.isalnum())
#   using slicing for the palindrome evaluation.
    if edited[0::1] == edited[::-1]:
        print(f"yes, {item} is a palindrome.")
    else:
        print(f"no, {item} is not a palindrome.")