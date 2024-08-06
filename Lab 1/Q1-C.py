# Given message
sent = "Iamlearninginformationsecurity"

# Keys
a = 15
b = 20
# Multiplicative inverse of a mod 26
a_inv = 7

# Encryption process
encmsg = ""
for ch in sent:
    asc = ord(ch)
    if 65 <= asc <= 90:  # Uppercase letters
        enc = ((a * (asc - 65) + b) % 26) + 65
        encmsg += chr(enc)
    elif 97 <= asc <= 122:  # Lowercase letters
        enc = ((a * (asc - 97) + b) % 26) + 97
        encmsg += chr(enc)
    else:
        encmsg += ch  # Non-alphabetic characters unchanged

print("Encrypted message: ", encmsg)

# Decryption process
decmsg = ""
for ch in encmsg:
    asc = ord(ch)
    if 65 <= asc <= 90:  # Uppercase letters
        dec = (a_inv * (asc - 65 - b) % 26 + 26) % 26 + 65
        decmsg += chr(dec)
    elif 97 <= asc <= 122:  # Lowercase letters
        dec = (a_inv * (asc - 97 - b) % 26 + 26) % 26 + 97
        decmsg += chr(dec)
    else:
        decmsg += ch  # Non-alphabetic characters unchanged

print("Decrypted message: ", decmsg)
