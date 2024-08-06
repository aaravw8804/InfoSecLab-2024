#Encryption
sent = "Iamlearninginformationsecurity"
encmsg = ""
for ch in sent:
    asc = ord(ch)
    if 65 <= asc <= 90:
        asc = (((asc-65)+20)%26)+65
        ench = chr(asc)
        encmsg+=ench
    elif 97 <= asc <= 122:
        asc = (((asc-97)+20)%26)+97
        ench = chr(asc)
        encmsg+=ench
    else:
        encmsg+=ch
print("Encrypted message: ",encmsg)

#Decryption
decmsg = ""

for ch in encmsg:
    asc = ord(ch)
    if 65 <= asc <= 90:  # Check if the character is an uppercase letter
        asc = (((asc - 65) - 20) % 26) + 65
        dech = chr(asc)
        decmsg += dech
    elif 97 <= asc <= 122:  # Check if the character is a lowercase letter
        asc = (((asc - 97) - 20) % 26) + 97
        dech = chr(asc)
        decmsg += dech
    else:
        # Add non-alphabetic characters unchanged
        decmsg += ch

print("Decrypted message: ", decmsg)