def crc8(data):
    n = len(data)
    word = int(data, 2) # Convert binary string to an integer
    div = 139 # CRC-8 divisor 10001011 in binary
    word <<= 7 # Left shift by 7 bits (same as adding 7 zeroes)
    check = 1 << (n + 7 - 1) # Bitmask to check the first digit
    div <<= (n - 1) # Align divisor with the current dividend
    res = word
    
    for i in range(n):
        if res & check:
            res ^= div # XOR with the divisor if the leftmost bit is 1
        div >>= 1
        check >>= 1 # Move to the next bit position
    
    return word ^ res # Return the CRC (remainder)

data = input("Enter the binary number for CRC8: ")
print('Code word using crc8:', bin(crc8(data)))

def checkCrc(new_data):
    n = len(new_data)
    word = int(new_data, 2) # Convert binary string to an integer
    print("Dataword is:", bin(word))
    code = crc8(new_data)
    print("Codeword is:", bin(code))
    
    div = 139 # CRC-8 divisor 10001011 in binary
    check = 1 << (n + 7 - 1) # Bitmask to check the first digit
    div <<= (n - 1) # Align divisor with the current dividend
    res = code
    
    for i in range(n):
        if res & check:
            res ^= div # XOR with the divisor if the leftmost bit is 1
        div >>= 1
        check >>= 1 # Move to the next bit position
    
    return res == 0 # Return True if no errors, False otherwise

new_data = input("Enter dataword for CRC checking: ")
if checkCrc(new_data):
    print('No errors in data check')
else:
    print('Error in data check')
