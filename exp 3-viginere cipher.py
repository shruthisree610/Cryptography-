def vigenere(text, key, mode):
    result = ""
    key = key.upper()
    for i in range(len(text)):
        if text[i].isalpha():
            if mode == "e":   # encrypt
                val = (ord(text[i].upper()) + ord(key[i % len(key)]) - 2*65) % 26
            else:            # decrypt
                val = (ord(text[i].upper()) - ord(key[i % len(key)]) + 26) % 26
            result += chr(val + 65)
        else:
            result += text[i]
    return result


choice = input("Encrypt or Decrypt? (e/d): ").lower()
text = input("Enter text: ")
key = input("Enter key: ")

output = vigenere(text, key, choice)
print("Result:", output)
