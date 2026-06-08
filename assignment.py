print("hi ma am kelechukwu.this is my first")
print("ASSIGNMENT")
import time
import sys

name = "Miracle Obike"

message = f"Hello, {name}! Welcome 😊"

# Simple loading animation
print("Loading your message", end="")

for i in range(10):
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.3)

print("\n\n")

# Typing effect
for char in message:
    print(char, end="")
    sys.stdout.flush()
    time.sleep(0.08)

print("\n\nHave a great day 🚀")
print('nwosu onyeka vivian')
my_list = ['mummy',
           'hannah', 
           'murder for a jarof red rum',
           'mom', 'seagull', 'tomato', 
           'no lemon, no melon',
           'some men interpret nine memos',
           'madam']

for item in my_list:
    if item == item[::-1]: 
      print("Is palindrome " + item)  

    else:
       print("Is not palindrome " + item)
my_list = [
    'mummy','hannah','murder for a jar of red rum','mom',
    'seagull','tomato','no lemon','no melon',
    'some men interpret nine memos','madam']

for item in my_list:
    cleaned = item.replace(" ", "")
    
    if cleaned == cleaned[::-1]:
        print (item, "is Palindrome")
    else:
        print (item, "is not a Palindrome")
        
# determination of palindrome using the following words, phrase in the list below.
dera_list =  ['mummy', 'hannah', 'murder for a jar of red rum', 'mom', 'seagull', 'tomato', 'no lemon, no melon', 'some men interpret nine memos', 'madam' ]
for z in dera_list:

    z_length = len(z)
    z_inverse = z[-1:-(z_length+1):-1]
    if z ==z_inverse:
            print(f"{z} is a palindrome")
    else:
            print(f"{z} is not a palindrome")
