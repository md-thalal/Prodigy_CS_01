def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        # Check if character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
plaintext = input("Enter the Text : ")
shift = int(input("Enter the shift value : "))
encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)
