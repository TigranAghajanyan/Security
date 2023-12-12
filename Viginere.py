def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        plain_char = ord(plain_text[i])
        key_char = ord(key[i % key_length])
        encrypted_char = (plain_char + key_char) % 26 + 65
        encrypted_text += chr(encrypted_char)

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        encrypted_char = ord(encrypted_text[i])
        key_char = ord(key[i % key_length])
        decrypted_char = (encrypted_char - key_char + 26) % 26 + 65
        decrypted_text += chr(decrypted_char)

    return decrypted_text

# Пример использования:
plaintext = "HELLOWORLD"
encryption_key = "KEY"

encrypted_text = vigenere_encrypt(plaintext, encryption_key)
decrypted_text = vigenere_decrypt(encrypted_text, encryption_key)

print("Input text:", plaintext)
print("encode text:", encrypted_text)
print("decode text:", decrypted_text)
