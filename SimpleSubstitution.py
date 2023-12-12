import string
import random

class SimpleSubstitutionCipher:
    def __init__(self):
        self.plaintext_alphabet = list(string.ascii_lowercase)
        self.ciphertext_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        ciphertext_alphabet = list(string.ascii_lowercase)
        random.shuffle(ciphertext_alphabet)
        return ciphertext_alphabet

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext.lower():
            if char.isalpha():
                index = self.plaintext_alphabet.index(char)
                encrypted_text += self.ciphertext_alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext.lower():
            if char.isalpha():
                index = self.ciphertext_alphabet.index(char)
                decrypted_text += self.plaintext_alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text

# Example usage
cipher = SimpleSubstitutionCipher()
plaintext = "Hello, this is a simple substitution cipher example!"
encrypted_text = cipher.encrypt(plaintext)
decrypted_text = cipher.decrypt(encrypted_text)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
