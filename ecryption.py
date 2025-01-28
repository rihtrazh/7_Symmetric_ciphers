from collections import Counter
import random

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

def crack_caesar_cipher(encrypted_text):
    frequency = Counter(filter(str.isalpha, encrypted_text.lower()))
    most_common_letter = frequency.most_common(1)[0][0]
    assumed_shift = ord(most_common_letter) - ord('e')
    return caesar_decrypt(encrypted_text, assumed_shift)

def vernam_encrypt(text, key):
    return "".join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

def vernam_decrypt(encrypted_text, key):
    return vernam_encrypt(encrypted_text, key)

def generate_vernam_key(length):
    return ''.join(chr(random.randint(0, 127)) for _ in range(length))

caesar_text = "Hello, World!"
caesar_shift = 3
encrypted_caesar_text = caesar_encrypt(caesar_text, caesar_shift)
decrypted_caesar_text = caesar_decrypt(encrypted_caesar_text, caesar_shift)
cracked_caesar_text = crack_caesar_cipher(encrypted_caesar_text)

vernam_text = "Secret Message"
vernam_key = generate_vernam_key(len(vernam_text))
encrypted_vernam_text = vernam_encrypt(vernam_text, vernam_key)
decrypted_vernam_text = vernam_decrypt(encrypted_vernam_text, vernam_key)

print("Шифр Цезаря")
print("Исходный текст ", caesar_text)
print("Зашифрованный текст ", encrypted_caesar_text)
print("Дешифрованный текст ", decrypted_caesar_text)
print("Восстановленный текст без ключа ", cracked_caesar_text)
print("\n")

print("Шифр Вернама")
print("Исходный текст ", vernam_text)
print("Случайный ключ ", vernam_key)
print("Зашифрованный текст ", encrypted_vernam_text)
print("Дешифрованный текст ", decrypted_vernam_text)
