My_list = ["mummy", "hannah", "murder for a jar of red rum", "mom", "sea gull", "tomato", "nolemonnomelon", "some men interpret nine memos", "madam"]
for item in My_list:
    clean_item = item.replace(" ", " ").replace(",", "").lower()
    reversed_item = clean_item[::-1]
    if clean_item == reversed_item:
        print(item, "is palindrome.")
    else:
        print(item, "is not a palindrome.")