import sys
import time

list1 = []
print("--- list 1 ---")
    
user_input = input("enter an input: ")
list1.append(user_input)
while True:
        
    through = input("Are you through? (yes/no): ").strip()
    if through == 'yes':
        break
    elif through == 'no':
        more = input('Continue typing: ')
        list1.append(more)
    else:
        print("invalid response")
    
list2 = []
print('--- list 2 ---  ')
user_input = input("enter an input: ")
list2.append(user_input)
    
while True:
    
    through = input("Are you through? (yes/no): ").strip()
    if through == 'yes':
        break
    elif through == 'no':
        more = input('Continue typing: ')
        list2.append(more)
    else:
        print("invalid response")
    
if len(list1) != len(list2):
    print("length of lists dont match")
    sys.exit()
else:
    print( "lengths match. proceeding")
        
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
            
    result_dict = dict(zip(list1, list2))
    print(result_dict)