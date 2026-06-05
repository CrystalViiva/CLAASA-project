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