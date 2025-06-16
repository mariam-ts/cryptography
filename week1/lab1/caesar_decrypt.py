# caesar_decrypt.py

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted += char
    return decrypted

if __name__ == "__main__":
    ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    ciphertext2 = "mznxpz"
    for shift in range(1, 26):
        print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")
    for shift in range(1, 26):
        print(f"Shift {shift}: {caesar_decrypt(ciphertext2, shift)}")
        


# The Caesar Cipher is insecure because it uses a simple substitution method with 
# only 25 possible key variations, making it easily breakable through brute-force 
# or frequency analysis. Since the encryption pattern remains consistent, common 
# letters like 'E' remain the most frequent, allowing cryptanalysts to reverse it quickly. 
# While it's useful for learning purposes, modern cryptographic needs far exceed its capabilities. 
# However, similar forms of encryption may still exist in some legacy systems—like old ATMs or 
# embedded devices—that rely on symmetric encryption principles but haven’t been upgraded to stronger 
# algorithms.

