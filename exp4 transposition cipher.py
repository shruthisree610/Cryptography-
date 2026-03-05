# Transposition Cipher

text = input("Enter the message: ")
key = int(input("Enter numeric key: "))

choice = input("E for Encrypt, D for Decrypt: ").upper()

if choice == 'E':
    result = ""
    for i in range(key):
        for j in range(i, len(text), key):
            result += text[j]
    print("Encrypted text:", result)

elif choice == 'D':
    result = [''] * key
    col_len = len(text) // key
    extra = len(text) % key
    index = 0

    for i in range(key):
        length = col_len + 1 if i < extra else col_len
        result[i] = text[index:index+length]
        index += length

    decrypted = ""
    for i in range(max(len(r) for r in result)):
        for r in result:
            if i < len(r):
                decrypted += r[i]

    print("Decrypted text:", decrypted)

else:
    print("Invalid choice")
