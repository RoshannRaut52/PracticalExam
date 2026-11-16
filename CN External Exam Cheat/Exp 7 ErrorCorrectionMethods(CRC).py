# CRC (Cyclic Redundancy Check)

data = input("Enter data bits: ")
divisor = input("Enter generator bits: ")

# Append zeros to data
n = len(divisor)
temp = list(data + '0' * (n - 1))

# Perform binary division using XOR
for i in range(len(data)):
    if temp[i] == '1':
        for j in range(n):
            temp[i + j] = str(int(temp[i + j]) ^ int(divisor[j]))

# Get CRC remainder
remainder = ''.join(temp[-(n - 1):])

# Generate transmitted data
codeword = data + remainder

print("CRC Remainder:", remainder)
print("Transmitted Data:", codeword)

# Receiver side checking
temp = list(codeword)

for i in range(len(data)):
    if temp[i] == '1':
        for j in range(n):
            temp[i + j] = str(int(temp[i + j]) ^ int(divisor[j]))

check = ''.join(temp[-(n - 1):])

print("Receiver Remainder:", check)

if '1' not in check:
    print("No Error Detected")
else:
    print("Error Detected")