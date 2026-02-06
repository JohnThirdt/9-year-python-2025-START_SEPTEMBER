# Шифр Цезаря

def caesar(text, shift):
    result = ""
    for char in text.lower():
        if char.isalpha():
            new_pos = (ord(char) - ord('a') + shift) % 26
            result += chr(ord('a') + new_pos)
        else:
            result += char
    return result

print(caesar("hello", 3))

print(caesar("khoor", -3))