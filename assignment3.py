list1 = []
list2 = []
while True:
    value = input("Enter item for list1: ")
    list1.append(value)
    done = input("Are you through? (yes/no): ")
    if done == "yes":
        break

while True:
    value = input("Enter item for list2: ")
    list2.append(value)
    done = input("Are you through? (yes/no): ")
    if done == "yes":
        break
    if len(list1) != len(list2):
        print("length of lists don't match")
        exit()
    else:
        print("lenghts match. Proceeding")
        import time
        
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

result = dict(zip(list1, list2))
print(result)
print("PROGRAM ENDED SUCCESSFULLY")