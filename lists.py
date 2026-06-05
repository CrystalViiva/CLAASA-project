#To help the program recognise the time function
import time

#Create lists
list1 =  []
list2 = []

#To populte the first list
print("Enter items for this list")
while True:
    item = input("Enter an item: ")
    list1.append(item)
    
    done =  input("Are you through? (yes/no): ").lower()
    if done == "yes":
        break
    
#To populte the second list
print("\nEnter items for this list")
while True:
    item = input("Enter an item: ")
    list2.append(item)
    
    done = input("Are you through? (yes/no): ").lower()
    if done == "yes":
        break

#To check the lengths
if len(list1) != len(list2):
    print("Length of lists do not match")
else:
    print("Lengths match. Proceeding", end="")
    
    for _ in range(3):
        time.sleep(2)
        print(".", end="", flush=True)
        
        print()
        
#To create dictionary
result_dict = dict(zip(list1, list2))

print("\nDictionary:")
print(result_dict)
    