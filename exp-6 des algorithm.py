from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = input("Enter 8-character key: ").encode()
choice = input("Enter E to Encrypt or D to Decrypt: ")

des = DES.new(key, DES.MODE_ECB)

if choice.upper() == 'E':
    text = input("Enter plain text: ").encode()
    cipher = des.encrypt(pad(text, 8))
    print("Encrypted Text:", cipher)

elif choice.upper() == 'D':
    cipher = eval(input("Enter encrypted text: "))
    plain = unpad(des.decrypt(cipher), 8)
    print("Decrypted Text:", plain.decode())

else:
    print("Invalid choice")
