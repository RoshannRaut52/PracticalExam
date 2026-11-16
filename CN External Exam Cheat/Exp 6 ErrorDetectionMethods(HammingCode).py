# Hamming Code using Even Parity

def encode(data):
    m = len(data)
    r = 0

    # Calculate the number of parity bits required.
    while 2 ** r < m + r + 1:
        r += 1

    n = m + r
    code = [0] * (n + 1)

    # Place data bits in non-parity positions.
    j = 0
    for i in range(1, n + 1):
        if i not in [1, 2, 4, 8, 16]:
            if j < m:
                code[i] = int(data[j])
                j += 1

    # Calculate parity bits using even parity.
    for i in range(r):
        pos = 2 ** i
        parity = 0

        for j in range(1, n + 1):
            if j & pos:
                parity ^= code[j]

        code[pos] = parity

    return code, r


def decode(code, r):
    n = len(code) - 1
    error = 0

    # Check parity bits to locate an error.
    for i in range(r):
        pos = 2 ** i
        parity = 0

        for j in range(1, n + 1):
            if j & pos:
                parity ^= code[j]

        if parity:
            error += pos

    if error == 0:
        print("No error detected.")
    else:
        print("Error detected at position:", error)

        # Correct the error by flipping the bit.
        code[error] ^= 1
        print("Error corrected.")

    # Extract the original data bits.
    original = ""
    for i in range(1, n + 1):
        if i not in [1, 2, 4, 8, 16]:
            original += str(code[i])

    print("Original Data:", original)


# Main program
data = input("Enter data bits: ")

if not data or any(bit not in "01" for bit in data):
    print("Enter valid binary data.")
else:
    code, r = encode(data)

    print("Hamming Code:", "".join(str(code[i]) for i in range(1, len(code))))

    position = int(input("Enter error position (0 for no error): "))

    if 1 <= position < len(code):
        code[position] ^= 1

    print("Received Code:", "".join(str(code[i]) for i in range(1, len(code))))

    decode(code, r)

    print("Corrected Code:", "".join(str(code[i]) for i in range(1, len(code))))