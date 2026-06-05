my_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]

def palindrome_checker():
    for x in my_list:
        x = x.replace(" ","")
        x = x.lower()
        x = x.replace(",","")
        
        word = x[::-1]
        if x == word:
            print( x + " " + "is a palindrome")
        else:
            print(x + " " + "is not a palindrome")
    
    print("done")
    
palindrome_checker()