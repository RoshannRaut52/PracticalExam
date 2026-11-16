# Bit Stuffing Program

data = input("Enter binary data: ")

stuffed = ""
count = 0

for bit in data:

    stuffed += bit

    if bit == '1':
        count += 1

        # Insert 0 after five consecutive 1s
        if count == 5:
            stuffed += '0'
            count = 0

    else:
        count = 0

print("Original Data:", data)
print("Stuffed Data:", stuffed)