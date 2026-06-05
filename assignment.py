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