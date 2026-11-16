# Character Stuffing
# F is the FLAG character and E is the ESCAPE character.

data = input("Enter data: ")

FLAG = 'F'
ESC = 'E'

stuffed = ""

for ch in data:

    # Insert ESC before FLAG or ESC characters.
    if ch == FLAG or ch == ESC:
        stuffed += ESC

    # Add the original character.
    stuffed += ch

print("Original Data:", data)
print("Stuffed Data :", stuffed)