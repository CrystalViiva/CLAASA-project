My_list = ["mummy", "hannah", "murder for a jar of red rum", "mom", "seagull", "tomato", "nolemonnomelon", "some men interpret nine memos", "madam"]
for item in My_list:
    clean_item = item.replace(" ", " ").replace(",", "").lower()
    reversed_item = clean_item[::-1]
    if clean_item == reversed_item:
        print(item, "is Palindrome. ")
    else:
        print(item, "is not a palindrome.")
        
#To write a cod that will take in a list and check if the individual members of the list are palindromes

#write a list of both palindromes and non-palindromes
items = input("Enter words seperated by spaces: ").split()


#write a program that conditions the response
for  word in items: 
    if word == word[::-1]:
        print(f"{word} is a Palindrome")
    else:
        print(f"{word} is not a Palindrome")
# Palindrome Checker

my_list = ["mummy", "hannah", "murder for a jar of red rum", "mom" "seagull", "tomato", "no lemon no melon", "some men interpret nine memos", "madam"]

for item in my_list:
    # clean the string: remove spaces and commas, convert to lowercase
    neat = item.lower().replace(" ", "").replace(",", "")

    # checking palindrome 
    if neat == neat[::-1]:
        print(f"{item} is a Palindrome")
    else:
        print (f"{item} is not a Palindrome")
        
 
 
# expected out put
# mummy is not a Palindrome
# hannah is a Palindrome
# murder for a jar of red rum is a Palindrome
# momseagull is not a Palindrome
# tomato is not a Palindrome
# no lemon no melon is a Palindrome
# some men interpret nine memos is a Palindrome
# madam is a Palindrome


