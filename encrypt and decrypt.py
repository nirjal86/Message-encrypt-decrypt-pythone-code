def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)

message =  input("Enter a message: ")
shift = 3

operation = input("Enter the code to encrypt the message: ")
encrypted_message = encrypt_message(message, shift)
print("Encrypted message:", encrypted_message)

operation = input("Enter 'bigyan' to decrypt the message: ")
decrypted_message = decrypt_message(encrypted_message, shift)
print("Decrypted message:", decrypted_message)