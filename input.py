import time

class_name = []
score = []

while True:
    name = input("write a name: ")
    class_name.append(name)

    done = input("are you done (yes/no): ").lower()
    if done not in ['yes', 'no']:
        print("pick yes or no")
        continue

    if done == "yes":
        break

name_len = len(class_name)
print(name_len)

while True:
    scores = int(input("input scores: "))
    score.append(scores)

    done = input("are you done (yes/no): ").lower()
    if done not in ['yes', 'no']:
        print("pick yes or no")
        continue

    if done == "yes" and len(score) == name_len:
        break

if len(class_name) != len(score):
    print("length of lists don't match")
else:
    period = "."
    print("lengths match. Proceeding")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    
    my_dict = dict(zip(class_name, score))
    print(my_dict)