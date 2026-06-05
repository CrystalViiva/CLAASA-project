#To write a cod that will take in a list and check if the individual members of the list are palindromes

#write a list of both palindromes and non-palindromes
items = input("Enter words seperated by spaces: ").split()


#write a program that conditions the response
for  word in items: 
    if word == word[::-1]:
        print(f"{word} is a Palindrome")
    else:
        print(f"{word} is not a Palindrome")