#Encryption
sent = "Iamlearninginformationsecurity"
encmsg = ""
for ch in sent:
    asc = ord(ch)
    if 65 <= asc <= 90:
        asc = (((asc-65)*15)%26)+65
        ench = chr(asc)
        encmsg+=ench
    elif 97 <= asc <= 122:
        asc = (((asc-97)*15)%26)+97
        ench = chr(asc)
        encmsg+=ench
    else:
        encmsg+=ch
print("Encrypted message: ",encmsg)

# Multiplicative inverse of 15 mod 26 is 7
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

inverse_key = mod_inverse(15, 26)
if inverse_key is None:
    raise ValueError("Multiplicative inverse not found")

decmsg = ""

for ch in encmsg:
    asc = ord(ch)
    if 65 <= asc <= 90:  # Check if the character is an uppercase letter
        asc = ((asc - 65) * inverse_key) % 26 + 65
        dech = chr(asc)
        decmsg += dech
    elif 97 <= asc <= 122:  # Check if the character is a lowercase letter
        asc = ((asc - 97) * inverse_key) % 26 + 97
        dech = chr(asc)
        decmsg += dech
    else:
        # Add non-alphabetic characters unchanged
        decmsg += ch

print("Decrypted message: ", decmsg)
